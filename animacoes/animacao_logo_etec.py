import pygame
from pygame.locals import *
from ui.texto import TextoFade
from config.constantes import (
    largura_tela, altura_tela,
    largura_pixel_tela, altura_pixel_tela
)


class Creditos_inicial(pygame.sprite.Sprite):
    """
    Exibe o logo da Etec + nome da escola com fade-in.
    Estados internos:
        'fade_in_logo'  → logo aparece
        'mostrando'     → logo visível por um tempo
        'saindo'        → logo desliza para a esquerda e some
        'concluido'     → animação terminou
    """

    DURACAO_MOSTRANDO_MS = 1500   # quanto tempo fica parado visível
    VELOCIDADE_SAIDA     = 8      # pixels por frame ao sair

    def __init__(self):
        super().__init__()

        # --- Logo da Etec ---
        self.sprite_etec = pygame.image.load("assets/imagens/logo_etec.png").convert_alpha()
        largura_logo = int(largura_tela * 0.20)
        altura_logo  = int(altura_tela  * 0.20)
        self.sprite_etec = pygame.transform.scale(self.sprite_etec, (largura_logo, altura_logo))
        self.rect_etec   = self.sprite_etec.get_rect(
            center=(largura_pixel_tela // 2, altura_pixel_tela // 2 - int(altura_pixel_tela * 0.05))
        )

        # --- Texto do nome ---
        self.texto = TextoFade(
            caminho_fonte  = "assets/fonts/Jersey15-Regular.ttf",
            tamanho        = 40,
            negrito        = False,
            italico        = False,
            antialias      = True,
            texto          = "Ilza Nascimento Pintus",
            cor            = (64, 84, 96),
            pos_x          = largura_pixel_tela // 2 - 150,
            pos_y          = altura_pixel_tela  // 2 + int(altura_pixel_tela * 0.08),
            largura_max    = largura_tela * 0.50,
        )

        # Estado da animação
        self.alpha         = 0
        self.estado        = 'fade_in_logo'
        self.tempo_parado  = 0
        self.concluido     = False

    # ------------------------------------------------------------------
    def update(self, tela):
        if self.concluido:
            return

        if self.estado == 'fade_in_logo':
            self.alpha = min(self.alpha + 4, 255)
            self.sprite_etec.set_alpha(self.alpha)
            tela.blit(self.sprite_etec, self.rect_etec)
            self.texto.update(tela)
            if self.alpha >= 255 and self.texto.concluido:
                self.estado       = 'mostrando'
                self.tempo_parado = pygame.time.get_ticks()

        elif self.estado == 'mostrando':
            tela.blit(self.sprite_etec, self.rect_etec)
            self.texto.update(tela)
            if pygame.time.get_ticks() - self.tempo_parado >= self.DURACAO_MOSTRANDO_MS:
                self.estado = 'saindo'

        elif self.estado == 'saindo':
            self.rect_etec.x    -= self.VELOCIDADE_SAIDA
            self.texto.rect.x   -= self.VELOCIDADE_SAIDA
            self.alpha = max(self.alpha - 5, 0)
            self.sprite_etec.set_alpha(self.alpha)
            self.texto.image.set_alpha(self.alpha)
            tela.blit(self.sprite_etec, self.rect_etec)
            tela.blit(self.texto.image,  self.texto.rect)
            if self.rect_etec.right < 0:
                self.concluido = True
