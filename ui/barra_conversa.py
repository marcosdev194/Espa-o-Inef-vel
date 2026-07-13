import pygame
from pygame.locals import *

class Barra_Conversa(pygame.sprite.Sprite):
    def __init__(self,largura_barra,altura_barra):
        super().__init__()
        self.Barra=pygame.image.load("")
        self.Barra=pygame.transform.scale(self.Barra,(largura_barra,altura_barra))
        self.rect_barra=self.Barra.get_rect()
        self.rect_barra.centerx=largura_barra//2
        self.rect_barra.midbottom=altura_barra

    def update(self,tela):
        tela.blit(self.Barra,self.rect_barra)