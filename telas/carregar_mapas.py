import pygame
from pygame.locals import *
from grupos.grupos_mapas import grupo_quartoc,quartoc
from grupos.grupos_sprite import grupo_fade_entrada,Cutscene_sprite
from config.config_janela import tela
from grupos.grupo_entidades import grupo_player
from grupos.grupos_mapas import grupo_corredor_casa
def Carregar_quarto():
    if Cutscene_sprite.concluido:
        grupo_fade_entrada.update(tela)
        
        grupo_quartoc.update(tela)
        grupo_player.update(tela)
    if quartoc.open_door:
        return True
    return False
def Carregar_corredor_casa():
    grupo_corredor_casa.update(tela)
    grupo_player.update(tela)
        





