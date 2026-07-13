import pygame
from pygame.locals import *
from entidades.player import Player
from config.constantes import largura_pixel_tela,altura_pixel_tela
from animacoes.obstaculo import criar_grupo_obstaculos
"""player=Player(100,100,(largura_pixel_tela,altura_pixel_tela))
grupo_player=pygame.sprite.Group()
grupo_player.add(player)"""

paredes_mapa_1 = [
    (0,0, largura_pixel_tela,140),  # parede de cima
    (0, altura_pixel_tela-110,largura_pixel_tela,110),  # parede de baixo
    (0,0,360, altura_pixel_tela),  # parede esquerda
    (largura_pixel_tela-360, 0,360, altura_pixel_tela),  # parede direita
]
cama_quarto=[
    (0,0,0,0),
    (0,0,0,0),
    (855,160,5,100),
    (920,160,50,100)
]
grupo_obstaculos_mapa_1 = criar_grupo_obstaculos(paredes_mapa_1)

 
player = Player(70, 70, (largura_pixel_tela, altura_pixel_tela), grupo_obstaculos_mapa_1)
grupo_player = pygame.sprite.Group()
grupo_player.add(player)