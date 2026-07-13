import pygame
from pygame.locals import *
from mapas.quarto_caleb import Quarto
from mapas.casa_corredor import Corredor_Casa
from config.constantes import largura_tela,altura_tela

"-------quarto---------"
quartoc=Quarto(largura_tela,altura_tela)
grupo_quartoc=pygame.sprite.Group()
grupo_quartoc.add(quartoc)

"-----corrdor---------"
mapa_corredor=Corredor_Casa()
grupo_corredor_casa=pygame.sprite.Group()
grupo_corredor_casa.add(mapa_corredor)
