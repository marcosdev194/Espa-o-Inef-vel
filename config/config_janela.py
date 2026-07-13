import pygame
from pygame.locals import *

# pygame.init() é chamado APENAS no main.py — nunca aqui

fullscreen = True
info = pygame.display.Info()
largura_tela = info.current_w
altura_tela  = info.current_h

pygame.display.set_caption("O espaço inefável")
tela = pygame.display.set_mode((largura_tela, altura_tela))


def tamanho_tela():
    return tela.get_size()


def escala(escala_largura, escala_altura):
    """Retorna fatores de escala em relação à resolução atual."""
    fx = largura_tela / (largura_tela * escala_largura)
    fy = altura_tela  / (altura_tela  * escala_altura)
    return fx, fy


def mudar_tamanho_tela():
    global tela, fullscreen
    fullscreen = not fullscreen
    if fullscreen:
        tela = pygame.display.set_mode((largura_tela, altura_tela), FULLSCREEN)
    else:
        tela = pygame.display.set_mode(
            (int(largura_tela * 0.90), int(altura_tela * 0.90))
        )
    return tela
