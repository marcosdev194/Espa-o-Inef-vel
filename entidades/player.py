import pygame
from pygame.locals import *



class Player(pygame.sprite.Sprite):
    """
    Personagem com 4 direções de movimento (W/A/S/D) e duas sprite sheets:
    uma para andando, outra para parado.

    Cada sheet tem 12 frames organizados em 4 blocos de 3 frames:
        índices 0-2  → frente
        índices 3-5  → esquerda
        índices 6-8  → direita
        índices 9-11 → costas
    """

    VELOCIDADE_ANIMACAO = 0.2   # quão rápido os frames avançam
    VELOCIDADE_MOVIMENTO = 2    # pixels por frame ao andar

    # Faixa de frames (início, fim) para cada direção — usado tanto
    # para a sheet de andando quanto para a de parado.
    FAIXAS_DIRECAO = {
        'frente':   (0, 2),
        'esquerdo': (3, 5),
        'direito':  (6, 8),
        'costas':   (9, 11),
    }

    def __init__(self, largura_perso, altura_perso, pos=tuple, grupo_obstaculos=None):
        super().__init__()

        # Grupo de colisão — pode ser None se o mapa ainda não tiver obstáculos.
        # Trocar de mapa = passar um grupo_obstaculos diferente aqui, nada
        # dentro do Player precisa mudar.
        self.grupo_obstaculos = grupo_obstaculos

        self.sheet_andando = pygame.image.load("assets/imagens/entidade/player.png").convert_alpha()
        self.sheet_parado  = pygame.image.load("assets/imagens/entidade/player_parado.png").convert_alpha()

        self.sprites_andando = []
        self.sprites_parado  = []

        for i in range(12):
            area = pygame.Rect(i * 16, 0, 16, 16)

            frame_andando = self.sheet_andando.subsurface(area)
            frame_andando = pygame.transform.scale(frame_andando, (largura_perso, altura_perso))
            self.sprites_andando.append(frame_andando)

            frame_parado = self.sheet_parado.subsurface(area)
            frame_parado = pygame.transform.scale(frame_parado, (largura_perso, altura_perso))
            self.sprites_parado.append(frame_parado)

        # ── Estado da animação ────────────────────────────────────────────────
        # IMPORTANTE: cada direção tem o SEU PRÓPRIO contador de frame.
        # Isso é o que resolve o bug do "frame da direção anterior" —
        # trocar de direção não interfere mais no progresso da animação
        # de outra direção, porque elas não compartilham mais a mesma variável.
        self.frame_por_direcao = {
            'frente':   0.0,
            'esquerdo': 0.0,
            'direito':  0.0,
            'costas':   0.0,
        }

        self.andando = False
        self.direcao = 'frente'   # direção inicial — também usada quando parado
        self.image   = self.sprites_parado[0]
        self.rect    = self.image.get_rect(center=(pos[0] // 2, pos[1] // 2))

    # ── Movimento com colisão ────────────────────────────────────────────────

   

    # ── Animação ──────────────────────────────────────────────────────────────

    def _avancar_frame(self, lista_sprites):
        """
        Avança o frame da direção atual (self.direcao) dentro da faixa
        correspondente, usando o contador PRÓPRIO daquela direção.
        """
        inicio, fim = self.FAIXAS_DIRECAO[self.direcao]

        frame_atual = self.frame_por_direcao[self.direcao]
        frame_atual += self.VELOCIDADE_ANIMACAO

        if frame_atual >= fim + self.VELOCIDADE_ANIMACAO:
            frame_atual = inicio

        self.frame_por_direcao[self.direcao] = frame_atual

        frame_index = int(frame_atual)
        self.image  = lista_sprites[frame_index]

    def mover_com_colisao(self,dx,dy):
    

        if self.grupo_obstaculos is None:
            # Sem mapa de colisão carregado ainda — move livremente
            self.rect.x += dx
            self.rect.y += dy
            return

        # Move no eixo X e desfaz SÓ esse eixo se colidir
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self.grupo_obstaculos):
            self.rect.x -= dx

        
        # Move no eixo Y e desfaz SÓ esse eixo se colidir
        self.rect.y += dy
        if pygame.sprite.spritecollideany(self.grupo_obstaculos):
            self.rect.y -= dy


    def evento_player(self):
        teclas = pygame.key.get_pressed()

        if teclas[K_w]:
            self.andando = True
            self.direcao = 'costas'
        elif teclas[K_s]:
            self.andando = True
            self.direcao = 'frente'
        elif teclas[K_a]:
            self.andando = True
            self.direcao = 'esquerdo'
        elif teclas[K_d]:
            self.andando = True
            self.direcao = 'direito'
        else:
            self.andando = False
            # self.direcao NÃO muda aqui — mantém a última direção
            # para saber qual sprite "parado" mostrar (Bug 1 corrigido)

    # ── Update principal ──────────────────────────────────────────────────────

    def update(self, tela):
        self.evento_player()

        if self.andando:
            self._avancar_frame(self.sprites_andando)

            if self.direcao == 'costas':
                self.mover_com_colisao(0, -self.VELOCIDADE_MOVIMENTO)
            elif self.direcao == 'frente':
                self.mover_com_colisao(0, self.VELOCIDADE_MOVIMENTO)
            elif self.direcao == 'esquerdo':
                self.mover_com_colisao(-self.VELOCIDADE_MOVIMENTO, 0)
            elif self.direcao == 'direito':
                self.mover_com_colisao(self.VELOCIDADE_MOVIMENTO, 0)
            #self.rect.y -= dy

        else:
            # Parado: usa a sheet de "parado", na faixa da última direção usada
            self._avancar_frame(self.sprites_parado)

        tela.blit(self.image, self.rect)