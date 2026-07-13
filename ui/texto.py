import pygame
from pygame.locals import *


def quebrar_texto(texto, fonte, largura_max):
    """Divide o texto em linhas que cabem dentro de largura_max."""
    palavras = texto.split()
    linhas = []
    linha_atual = ""
    for palavra in palavras:
        teste = linha_atual + palavra + " "
        if fonte.size(teste)[0] <= largura_max:
            linha_atual = teste
        else:
            linhas.append(linha_atual)
            linha_atual = palavra + " "
    linhas.append(linha_atual)
    return linhas


class TextoFade(pygame.sprite.Sprite):
    """
    Texto que aparece gradualmente (fade-in) a cada frame.
    Use dentro de um sprite Group chamando update(tela).
    """

    def __init__(self, caminho_fonte, tamanho, negrito, italico, antialias,
                 texto, cor, pos_x, pos_y, largura_max):
        super().__init__()
        fonte = pygame.font.Font(caminho_fonte, tamanho)
        linhas = quebrar_texto(texto, fonte, largura_max)

        # Monta uma Surface que contenha todas as linhas
        surfaces = [fonte.render(l, antialias, cor) for l in linhas]
        largura = max(s.get_width() for s in surfaces)
        altura_total = len(surfaces) * (tamanho + 4)

        self.image = pygame.Surface((largura, altura_total), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        for i, s in enumerate(surfaces):
            self.image.blit(s, (0, i * (tamanho + 4)))

        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
        self.alpha = 0
        self.concluido = False

    def update(self, tela):
        if self.concluido:
            tela.blit(self.image, self.rect)
            return
        self.alpha = min(self.alpha + 3, 255)
        self.image.set_alpha(self.alpha)
        tela.blit(self.image, self.rect)
        if self.alpha >= 255:
            self.concluido = True
