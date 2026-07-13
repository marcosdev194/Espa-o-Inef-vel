import pygame
from pygame.locals import *


class Tela_de_carregamento(pygame.sprite.Sprite):
    """
    Fluxo ao clicar:
        esperando → indo_dir → voltando_centro → indo_esq → voltando_centro2
        → esperando  (pode clicar de novo)

    Clicando durante a animação: ignorado (estado != 'esperando').

    Ao clicar enquanto a porta está aberta (estado 'aberta'):
        aberta → zoom → clareando → escurecendo → concluido
    """

    VELOCIDADE_GIRO  = 6     # graus por frame
    ANGULO_MAX       = 45    # graus de cada lado
    VELOCIDADE_ZOOM  = 0.03  # fator de escala por frame
    VELOCIDADE_FADE  = 4     # alpha por frame

    def __init__(self, largura_porta, altura_porta, largura_tela, altura_tela):
        super().__init__()

        self.largura_tela = largura_tela
        self.altura_tela  = altura_tela
        self.centro_tela  = (largura_tela // 2, altura_tela // 2)

        # ── Sprites ──────────────────────────────────────────────────────────
        self.sheet = pygame.image.load("assets/imagens/porta.png").convert_alpha()
        lista_portas = []
        for i in range(2):
            area  = pygame.Rect(i * 19, 0, 19, 35)
            frame = self.sheet.subsurface(area)
            frame = pygame.transform.scale(frame, (largura_porta, altura_porta))
            lista_portas.append(frame)

        self.image_original = lista_portas[0]   # porta fechada
        self.image_aberta   = lista_portas[1]   # porta aberta

        self.image = self.image_original.copy()
        self.rect  = self.image.get_rect(center=self.centro_tela)

        # ── Fade ─────────────────────────────────────────────────────────────
        self.fade_surf  = pygame.Surface((largura_tela, altura_tela))
        self.fade_alpha = 0

        # ── Estado ───────────────────────────────────────────────────────────
        self.estado    = 'esperando'
        self.angulo    = 0.0
        self.zoom      = 1.0
        self.hover     = False
        self.concluido = False
        self.num_click=0


        # Flag controlada externamente por carregar_animacoes.py
        # Quando True, o próximo clique abre a porta em vez de balançar
        self.carregamento_concluido = False

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _aplicar_rotacao(self, imagem_base):
        """Rotaciona sempre a partir da imagem original para evitar distorção."""
        self.image = pygame.transform.rotate(imagem_base, self.angulo)
        self.rect  = self.image.get_rect(center=self.centro_tela)

    def _aplicar_zoom(self, imagem_base):
        w = max(int(imagem_base.get_width()  * self.zoom), 1)
        h = max(int(imagem_base.get_height() * self.zoom), 1)
        self.image = pygame.transform.scale(imagem_base, (w, h))
        self.rect  = self.image.get_rect(center=self.centro_tela)

    # ── Eventos ──────────────────────────────────────────────────────────────

    def verificar_click_porta(self, event):
        """Chame no loop de eventos do main.py."""
        if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
            return
        if not self.rect.collidepoint(event.pos):
            return
        self.num_click+=1

        if self.estado == 'esperando':
            # Se o carregamento terminou, abre a porta; senão balança
            if self.carregamento_concluido:
                self.estado = 'abrindo'
            else:
                self.estado = 'indo_dir'

    # ── Update ───────────────────────────────────────────────────────────────

    def update(self, tela):
        if self.concluido:
            return

        self.hover = (self.estado == 'esperando' and
                      self.rect.collidepoint(pygame.mouse.get_pos()))

        tela.fill((0, 0, 0))
        

        # ── Máquina de estados ────────────────────────────────────────────────

        if self.estado == 'esperando':
            self.image = self.image_original.copy()
            if self.hover:
                brilho = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
                brilho.fill((255, 255, 255, 40))
                self.image.blit(brilho, (0, 0))
            self.rect = self.image.get_rect(center=self.centro_tela)

        elif self.estado == 'indo_dir':
            # Gira rápido para a direita até ANGULO_MAX
            self.angulo = min(self.angulo + self.VELOCIDADE_GIRO, self.ANGULO_MAX)
            self._aplicar_rotacao(self.image_original)
            if self.angulo >= self.ANGULO_MAX:
                self.estado = 'voltando_centro'  # vai voltar ao meio

        elif self.estado == 'voltando_centro':
            # Volta rapidamente para 0°
            self.angulo = max(self.angulo - self.VELOCIDADE_GIRO, 0)
            self._aplicar_rotacao(self.image_original)
            if self.angulo <= 0:
                self.estado = 'indo_esq'   # agora vai para a esquerda

        elif self.estado == 'indo_esq':
            # Gira rápido para a esquerda até -ANGULO_MAX
            self.angulo = max(self.angulo - self.VELOCIDADE_GIRO, -self.ANGULO_MAX)
            self._aplicar_rotacao(self.image_original)
            if self.angulo <= -self.ANGULO_MAX:
                self.estado = 'voltando_centro2'

        elif self.estado == 'voltando_centro2':
            # Volta para 0° e fica esperando de novo
            self.angulo = min(self.angulo + self.VELOCIDADE_GIRO, 0)
            self._aplicar_rotacao(self.image_original)
            if self.angulo >= 0:
                self.angulo = 0
                if self.num_click==5:
                    self.estado = 'abrindo'
                else:
                 self.estado = 'esperando'

        elif self.estado == 'abrindo':
            # Troca para sprite aberta e inicia zoom
            self.image  = self.image_aberta.copy()
            self.rect   = self.image.get_rect(center=self.centro_tela)
            self.estado = 'zoom'

        elif self.estado == 'zoom':
            self.zoom += self.VELOCIDADE_ZOOM
            self._aplicar_zoom(self.image_aberta)
            if (self.image.get_width()  >= self.largura_tela or
                self.image.get_height() >= self.altura_tela):
                self.estado     = 'clareando'
                self.fade_alpha = 0
                self.fade_surf.fill((255, 255, 255))

        elif self.estado == 'clareando':
            self._aplicar_zoom(self.image_aberta)
            self.fade_alpha = min(self.fade_alpha + self.VELOCIDADE_FADE, 255)
            self.fade_surf.set_alpha(self.fade_alpha)
            if self.fade_alpha >= 255:
                self.estado     = 'escurecendo'
                self.fade_alpha = 0           # começa o preto do zero
                self.fade_surf.fill((0, 0, 0))

        elif self.estado == 'escurecendo':
            velocidade      = self.VELOCIDADE_FADE * 3 if self.hover else self.VELOCIDADE_FADE
            self.fade_alpha = min(self.fade_alpha + velocidade, 255)
            self.fade_surf.set_alpha(self.fade_alpha)
            if self.fade_alpha >= 255:
                self.concluido = True
                return

        # ── Desenho ───────────────────────────────────────────────────────────
        tela.blit(self.image, self.rect)

        if self.estado in ('clareando', 'escurecendo'):
            tela.blit(self.fade_surf, (0, 0))