import pygame
from pygame.locals import *
from config.config_janela import *

# Clock — tick() é chamado no loop principal, não aqui
fps = pygame.time.Clock()

# Dimensões reais da janela em pixels
largura_pixel_tela, altura_pixel_tela = tamanho_tela()


# Fatores de escala
escala_largura, escala_altura = escala(0.90, 0.90)

# Escalas para elementos específicos
le_logo_etec,  ale_logo_etec  = escala(0.40, 0.40)
largura_nuvens_escala, altura_nuvens_escala = escala(0.85, 0.85)

le_botoes, ale_botoes=escala(0.90,0.60)
largura_botoes,altura_botoes=250,60

le_menu,ale_menu=escala(0.80,0.80)
le_barra_volume,ale_barra_volume=escala(0.30,0.30)
