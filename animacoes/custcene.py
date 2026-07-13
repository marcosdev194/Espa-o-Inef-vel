import pygame
from pygame.locals import *

class cutscene_embriao(pygame.sprite.Sprite):
    def __init__(self,largura_custcene,altura_cutscene):
        super().__init__()
        self.sheet=pygame.image.load("assets/imagens/embriao_sheet_custecene.png").convert()
        self.frames=[]
        for i in range(26):
            area=pygame.Rect(i*483,0,483,269)
            frame=self.sheet.subsurface(area)
            frame=pygame.transform.scale(frame,(largura_custcene,altura_cutscene))
            self.frames.append(frame)
        self.frame_atual=0
        self.ultimo_frame=len(self.frames)-1
        self.image=self.frames[0]
        self.rect=self.image.get_rect(center=(largura_custcene//2,altura_cutscene//2))
    #def aparecer_cutscene_embriao(self):
        self.MS_POR_FRAME=80
        self.ultimo_tick=pygame.time.get_ticks()
        self.concluido=False
        
    def update(self,tela):
        tela.fill((0,0,0))
        agora=pygame.time.get_ticks()
        if not self.concluido and agora - self.ultimo_tick>=self.MS_POR_FRAME:
            self.ultimo_tick=agora
            if self.frame_atual<self.ultimo_frame:
                self.frame_atual+=0.5
            else:
                self.concluido=True
        self.image=self.frames[int(self.frame_atual)]
        tela.blit(self.image,self.rect)
       
class Cutscene_olhos(pygame.sprite.Sprite):
    def __init__(self,largura_cutscene,altura_cutscene):
        super().__init__()
        self.lista_frames=[]
        self.sheet=pygame.image.load("assets/imagens/animacao_olho.png")
        for i in range(18):
            area=pygame.Rect(i*481,0,481,269)
            frame=self.sheet.subsurface(area)
            frame=pygame.transform.scale(frame,(largura_cutscene,altura_cutscene))
            self.lista_frames.append(frame)
        self.frame_atual=0
        self.ultimo_frame=len(self.lista_frames)-0.5
        self.image=self.lista_frames[0]
        self.rect=self.image.get_rect(center=(largura_cutscene//2,altura_cutscene//2))
        self.MS_FRAME=80
        self.ultimo_tick=pygame.time.get_ticks()
        self.concluido=False
    def update(self,tela):
        tela.fill((0,0,0))
        agora=pygame.time.get_ticks()
        if not self.concluido and agora - self.ultimo_tick>=self.MS_FRAME:
            self.ultimo_tick=agora
            if self.frame_atual<self.ultimo_frame:
                self.frame_atual+=0.5
            else:
                self.concluido=True
        self.image=self.lista_frames[int(self.frame_atual)]
        tela.blit(self.image,self.rect)