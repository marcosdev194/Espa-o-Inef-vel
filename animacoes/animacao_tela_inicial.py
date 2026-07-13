import pygame
from pygame.locals import *
import random
from config.constantes import (
    largura_tela, altura_tela,
    largura_pixel_tela, altura_pixel_tela
)


class Tela_inicial(pygame.sprite.Sprite):
    """Background da tela inicial com fade-in suave."""

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/imagens/tela_inicial.png").convert()
        self.image = pygame.transform.scale(self.image, (largura_tela, altura_tela))
        self.rect  = self.image.get_rect(topleft=(0, 0))
        self.alpha = 0
        self.saindo=False
        self.concluido=False
    def iniciar_saida(self):
        self.saindo=True

    def update(self, tela):
        if self.saindo:
            self.alpha=max(self.alpha-4,0)
            if self.alpha==0:
                self.concluido=True
        else:
           self.alpha = min(self.alpha + 4, 255)
        self.image.set_alpha(self.alpha)
        tela.blit(self.image, self.rect)


class Nome_jogo(pygame.sprite.Sprite):
    """Título do jogo com fade-in suave."""

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/imagens/titulo_inicial.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (int(largura_tela * 0.40), int(altura_tela * 0.40))
        )
        self.rect  = self.image.get_rect(
            center=(int(largura_pixel_tela * 0.50), int(altura_pixel_tela * 0.25))
        )
        self.alpha = 0
        self.saindo=False
    def iniciar_saida(self):
        self.saindo=True

    def update(self, tela):
        if self.saindo:
            self.alpha=max(self.alpha-4,0)
        else:
            self.alpha = min(self.alpha + 3, 255)
        self.image.set_alpha(self.alpha)
        tela.blit(self.image, self.rect)


class Nuvens_tela_inicial:
    """
    Duas fileiras de nuvens: esquerda → direita, direita → esquerda.
    Não é um Sprite pois possui duas listas de rects independentes.
    Chame Mover_nuvens() e depois Desenhar_nuvens() a cada frame.
    """

    VELOCIDADE = 2

    def __init__(self):
        self.image = pygame.image.load("assets/imagens/nuvem_teste.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (int(largura_tela * 0.18), int(altura_tela * 0.20))
        )
        larg_nuvem = self.image.get_width()

        self.esquerda = []
        self.direita  = []

        for i in range(5):
            r = self.image.get_rect()
            r.x = -larg_nuvem - i * int(largura_pixel_tela * 0.20)
            r.y = int(altura_pixel_tela * random.uniform(0.05, 0.35))
            self.esquerda.append(r)

        for i in range(5):
            r = self.image.get_rect()
            r.x = largura_pixel_tela + i * int(largura_pixel_tela * 0.20)
            r.y = int(altura_pixel_tela * random.uniform(0.05, 0.35))
            self.direita.append(r)

    def Mover_nuvens(self):
        for r in self.esquerda:
            r.x += self.VELOCIDADE
            if r.left > largura_pixel_tela:
                r.right = 0

        for r in self.direita:
            r.x -= self.VELOCIDADE
            if r.right < 0:
                r.left = largura_pixel_tela

    def Desenhar_nuvens(self, tela):
        for r in self.esquerda:
            tela.blit(self.image, r)
        for r in self.direita:
            tela.blit(self.image, r)


class Botao_inicial_play(pygame.sprite.Sprite):
    def __init__(self,largura_botoes,altura_botoes,pos_botoes=tuple,escalas=tuple):
        super().__init__()
        self.sheet=pygame.image.load("assets/imagens/botao_jogar.png").convert_alpha()
        self.frames=[]
        for i in range(15):
            area = pygame.Rect(i*90,0,90,42)
            frame=self.sheet.subsurface(area)
            frame=pygame.transform.scale(frame,(largura_botoes*escalas[0],altura_botoes*escalas[1]))
            self.frames.append(frame)
        self.frame_atual=0
        self.image=self.frames[0]
        self.ultimo_frame=len(self.frames)-0.5
        self.rect = self.image.get_rect(center=(pos_botoes[0]//5,pos_botoes[1]*0.80))
        self.foi_clicado=False


    def verificar_play(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            if self.rect.collidepoint(event.pos):
                self.foi_clicado=True

    def hover(self):
        if self.frame_atual<self.ultimo_frame:
            self.frame_atual+=0.5 
        self.image=self.frames[int(self.frame_atual)]
        

    def update(self,tela):
        pos_mouse=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos_mouse):
            self.hover()
        else:
            self.frame_atual=0
            self.image=self.frames[0]
        tela.blit(self.image,self.rect)
    

class Botao_inicial_configuracoes(pygame.sprite.Sprite):
    def __init__(self,largura_botoes,altura_botoes,pos_botoes=tuple,escalas=tuple):
        super().__init__()
        self.sheet=pygame.image.load("assets/imagens/botao_configuracao.png").convert_alpha()
        self.frames=[]
        for i in range(24):
            area = pygame.Rect(i*196,0,196,52)
            frame=self.sheet.subsurface(area)
            frame=pygame.transform.scale(frame,(largura_botoes*escalas[0],altura_botoes*escalas[1]))
            self.frames.append(frame)
        self.frame_atual=0
        self.image=self.frames[0]
        self.ultimo_frame=len(self.frames)-0.5
        self.rect = self.image.get_rect(center=(pos_botoes[0]//2,pos_botoes[1]*0.80))
        self.foi_clicado=False
    def hover(self):
        if self.frame_atual<self.ultimo_frame:
            self.frame_atual+=0.5 
        self.image=self.frames[int(self.frame_atual)]

    def verificar_config(self,event):
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if self.rect.collidepoint(event.pos):
                self.foi_clicado=True

    def update(self,tela):
        pos_mouse=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos_mouse):
            self.hover()
        else:
            self.frame_atual=0
            self.image=self.frames[0]
        tela.blit(self.image,self.rect)
        
        
class Botao_inicial_creditos(pygame.sprite.Sprite):
    def __init__(self,largura_botoes,altura_botoes,pos_botoes=tuple,escalas=tuple):
        super().__init__()
        self.sheet=pygame.image.load("assets/imagens/botao_credito.png").convert_alpha()
        self.frames=[]
        for i in range(21):
            area = pygame.Rect(i*127,0,127,47)
            frame=self.sheet.subsurface(area)
            frame=pygame.transform.scale(frame,(largura_botoes*escalas[0],altura_botoes*escalas[1]))
            self.frames.append(frame)
        self.frame_atual=0
        self.image=self.frames[0]
        self.ultimo_frame=len(self.frames)-0.5
        self.rect = self.image.get_rect(center=(pos_botoes[0]-(pos_botoes[0]//5),pos_botoes[1]*0.80))
        self.clicado_creditos=False
    def click_creditos(self,event):
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if self.rect.collidepoint(event.pos):
                self.clicado_creditos=True
    def hover(self):
        if self.frame_atual<self.ultimo_frame:
            self.frame_atual+=0.5 
        self.image=self.frames[int(self.frame_atual)]

    def update(self,tela):
        pos_mouse=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos_mouse):
            self.hover()
        else:
            self.frame_atual=0
            self.image=self.frames[0]
        tela.blit(self.image,self.rect)



