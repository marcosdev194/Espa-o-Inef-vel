import pygame
from pygame.locals import *
from grupos.grupo_entidades import player


class Quarto(pygame.sprite.Sprite):
    def __init__(self,largura_quarto,altura_quarto):
        super().__init__()
        self.background=pygame.image.load("assets/imagens/mapas_sprite/quarto.png").convert_alpha()
        self.background=pygame.transform.scale(self.background,(largura_quarto//2,altura_quarto//2+200))
        #self.rect_quarto=self.background.get_rect(topleft=(0,0))
        self.rect_quarto=self.background.get_rect(center=(largura_quarto//2,altura_quarto//2))
        self.porta=pygame.Rect(largura_quarto//2,altura_quarto-1,25,25)
        self.porta.midbottom=self.rect_quarto.midbottom
        self.open_door=False

    def update(self,tela):
        tela.fill((0,0,0))
        pygame.draw.rect(tela,(0,0,0),self.porta)
        if player.rect.colliderect(self.porta):
            print("colidiu")
            self.open_door=True
        else:
            self.open_door=False
        tela.blit(self.background,self.rect_quarto)
        

