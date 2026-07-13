import pygame
from pygame.locals import *


class Fade_in(pygame.sprite.Sprite):
    """Fade de transparente → opaco. Chame update(tela) a cada frame."""

    def __init__(self, largura_tela, altura_tela, cor_fundo=(255, 255, 255)):
        super().__init__()
        self.surface = pygame.Surface((largura_tela, altura_tela))
        self.surface.fill(cor_fundo)
        self.alpha = 0
        self.concluido = False

    def update(self, tela):
        if self.concluido:
            return
        self.alpha = min(self.alpha + 1, 255)
        self.surface.set_alpha(self.alpha)
        tela.blit(self.surface, (0, 0))
        if self.alpha >= 255:
            self.concluido = True

    def resetar(self):
        self.alpha = 0
        self.concluido = False


class Fade_out(pygame.sprite.Sprite):
    """Fade de opaco → transparente. Chame update(tela) a cada frame."""

    def __init__(self, largura_tela, altura_tela, cor_fundo=(255, 255, 255)):
        super().__init__()
        self.surface = pygame.Surface((largura_tela, altura_tela))
        self.surface.fill(cor_fundo)
        self.alpha = 255
        self.concluido = False

    def update(self, tela):
        if self.concluido:
            return
        self.alpha = max(self.alpha - 1, 0)
        self.surface.set_alpha(self.alpha)
        tela.blit(self.surface, (0, 0))
        if self.alpha <= 0:
            self.concluido = True

    def resetar(self):
        self.alpha = 255
        self.concluido = False
