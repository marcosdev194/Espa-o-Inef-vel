import pygame
from pygame.locals import *

class Creditos_iniciais(pygame.sprite.Sprite):
    def __init__(self,largura_menu,altura_menu,escalas=tuple,tela_pixel=tuple):
        super().__init__()
        largura_menu*=escalas[0]
        altura_menu*=escalas[1]
        self.background=pygame.image.load("assets/imagens/menu/background_menu.png")
        self.background=pygame.transform.scale(self.background,(largura_menu,altura_menu))
        self.rect_back=self.background.get_rect(center=(tela_pixel[0]//2,tela_pixel[1]//2))

        self.botao_exit=pygame.image.load("assets/imagens/menu/exit.png")
        self.botao_exit=pygame.transform.scale(self.botao_exit,(largura_menu*0.10,altura_menu*0.10))
        self.rect_exit=self.botao_exit.get_rect(topright=(self.rect_back.topright))
        self.exit_clicado=False
        self.creditos_aberto=False
    def verificar_click(self,event):
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if self.rect_exit.collidepoint(event.pos):
                self.exit_clicado=True
    def update(self,tela):
        
        tela.blit(self.background,self.rect_back)
        tela.blit(self.botao_exit,self.rect_exit)