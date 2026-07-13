import pygame
from pygame.locals import *
from config.constantes import le_menu,ale_menu,largura_pixel_tela,altura_pixel_tela


class Menu(pygame.sprite.Sprite):
    def __init__(self,largura_menu,altura_menu,escalas=tuple,tela_pixel=tuple):
        super().__init__()
        self.background=pygame.image.load("assets/imagens/menu/background_menu.png")
        largura_menu*=escalas[0]
        altura_menu*=escalas[1]
        self.background=pygame.transform.scale(self.background,(largura_menu,altura_menu))
        self.rect_back=self.background.get_rect(center=(tela_pixel[0]//2,tela_pixel[1]//2))

        self.botao_exit=pygame.image.load("assets/imagens/menu/exit.png")
        self.botao_exit=pygame.transform.scale(self.botao_exit,(largura_menu*0.10,altura_menu*0.10))
        self.rect_exit=self.botao_exit.get_rect(topright=self.rect_back.topright)
        self.menu_aberto=False
        self.exit_clicado=False

    def vexit_menu(self,event):
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if self.rect_exit.collidepoint(event.pos):
                self.exit_clicado=True
    def update(self,tela):
        tela.blit(self.background,self.rect_back)
        tela.blit(self.botao_exit,self.rect_exit)

menu=Menu(500,500,(le_menu,ale_menu),(largura_pixel_tela,altura_pixel_tela))
class Botao_inicio(pygame.sprite.Sprite):
    def __init__(self,largura_botao,altura_botao,escalas=tuple):
        super().__init__()
        self.image=pygame.image.load("assets/imagens/menu/inicio.png")
        self.image=pygame.transform.scale(self.image,(largura_botao*escalas[0],altura_botao*escalas[1]))
        
        self.rect=self.image.get_rect(bottomleft=menu.rect_back.bottomleft)
        self.clicado_inicio=False
    def click_inicio(self,event):
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if self.rect.collidepoint(event.pos):
                self.clicado_inicio=True

    def update(self,tela):
        tela.blit(self.image,self.rect)

class Botao_salvar(pygame.sprite.Sprite):
    def __init__(self,largura_botao,altura_botao,escalas=tuple):
        super().__init__()
        self.image=pygame.image.load("assets/imagens/menu/botao_salvar.png")
        self.image=pygame.transform.scale(self.image,(largura_botao*escalas[0],altura_botao*escalas[1]))
        self.rect=self.image.get_rect(midbottom=menu.rect_back.midbottom)
    def update(self,tela):
        tela.blit(self.image,self.rect)

class Botao_sair(pygame.sprite.Sprite):
    def __init__(self,largura_botao,altura_botao,escalas=tuple):
        super().__init__()
        self.image=pygame.image.load("assets/imagens/menu/botao_sair.png")
        self.image=pygame.transform.scale(self.image,(largura_botao*escalas[0],altura_botao*escalas[1]))
        self.rect=self.image.get_rect(bottomright=menu.rect_back.bottomright)
    def click_sair(self,event):
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if self.rect.collidepoint(event.pos):
                return True
        return False
    def update(self,tela):
        tela.blit(self.image,self.rect)

class Slider(pygame.sprite.Sprite):
    """
    Barra de volume arrastável.
 
    Como usar:
        slider = Slider(x=300, y=400, porcentagem_largura_tela=0.20)
        # no loop de eventos:
        slider.evento(event)
        # no loop de desenho:
        slider.update(tela)
        # para ler o volume (0.0 a 1.0):
        slider.volume
    """
 
    # Esses dois números definem o "desenho" do slider em proporção um ao outro.
    # Se quiser o botão maior ou menor em relação à barra, mude só este valor.
    ALTURA_BOTAO_RELATIVA_AO_FUNDO = 2.2   # botão é 2.2× mais alto que a barra
 
    def __init__(self, x, y, porcentagem_largura_tela=0.40):
        super().__init__()
        self.x = x
        self.y = y
        self.volume     = 0.5
        self.arrastando = False
 
        # ── Passo 1: carrega as imagens originais ───────────────────────────
        fundo_original = pygame.image.load("assets/imagens/menu/barra_menu.png").convert_alpha()
        botao_original = pygame.image.load("assets/imagens/menu/lua_botao.png").convert_alpha()
 
        # ── Passo 2: define o tamanho do FUNDO a partir da tela ─────────────
        # A largura da barra é uma % da largura da tela — isso resolve
        # o problema de não escalar com a resolução.
        largura_fundo = int(largura_pixel_tela * porcentagem_largura_tela)
 
        # A altura do fundo é calculada pela PRÓPRIA proporção da imagem,
        # então o fundo nunca fica esticado/achatado.
        proporcao_fundo = fundo_original.get_height() / fundo_original.get_width()
        altura_fundo    = int(largura_fundo * proporcao_fundo)
 
        self.fundo = pygame.transform.smoothscale(fundo_original, (largura_fundo, altura_fundo))
        self.largura_barra = largura_fundo   # guardamos para usar no arrasto depois
 
        # ── Passo 3: o BOTÃO usa o fundo como referência de tamanho ─────────
        # Em vez de você escolher um número solto para o botão, ele é definido
        # como "X vezes a altura do fundo" — por isso os dois sempre crescem
        # e encolhem JUNTOS, na mesma proporção, sem você precisar recalcular nada.
        altura_botao = int(altura_fundo * self.ALTURA_BOTAO_RELATIVA_AO_FUNDO)
 
        proporcao_botao = botao_original.get_width() / botao_original.get_height()
        largura_botao   = int(altura_botao * proporcao_botao)
 
        self.botao = pygame.transform.smoothscale(botao_original, (largura_botao, altura_botao))
 
        # ── Passo 4: posiciona os dois na tela ───────────────────────────────
        self.rect_fundo = self.fundo.get_rect(topleft=(x, y))
        self.rect_botao = self.botao.get_rect()
        self._atualizar_posicao_botao()
 
    # ── Métodos internos (o "_" na frente é convenção: "não chame de fora") ──
 
    def _atualizar_posicao_botao(self):
        """Recoloca o botão na posição X correspondente ao volume atual."""
        self.rect_botao.centerx = self.x + int(self.volume * self.largura_barra)
        self.rect_botao.centery = self.rect_fundo.centery
 
    def _calcular_volume_pela_posicao(self, mouse_x):
        """Converte a posição X do mouse num valor de volume entre 0.0 e 1.0."""
        mouse_x_dentro_dos_limites = max(self.x, min(mouse_x, self.x + self.largura_barra))
        return (mouse_x_dentro_dos_limites - self.x) / self.largura_barra
 
    # ── Métodos públicos — chame estes de fora da classe ──────────────────────
 
    def evento(self, event):
        """Chame dentro do loop de eventos do main.py."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect_botao.collidepoint(event.pos):
                self.arrastando = True
 
        elif event.type == pygame.MOUSEBUTTONUP:
            self.arrastando = False
 
        elif event.type == pygame.MOUSEMOTION:
            if self.arrastando:
                self.volume = self._calcular_volume_pela_posicao(event.pos[0])
                self._atualizar_posicao_botao()
 
    def update(self, tela):
        """Chame a cada frame para desenhar o slider."""
        tela.blit(self.fundo, self.rect_fundo)
        tela.blit(self.botao, self.rect_botao)
