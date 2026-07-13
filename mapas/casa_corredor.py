import pygame
from pygame.locals import *

class Corredor_Casa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image=pygame.image.load("")
        #self.rect=self.image.get_rect(center=(largura_corredor//2,altura_corredor//2))
    def update(self,tela):
        tela.fill((0,0,0))