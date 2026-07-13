import pygame


class Obstaculo(pygame.sprite.Sprite):
    """
    Bloco de colisão invisível — representa qualquer área sólida do mapa
    (parede, árvore, mesa, borda do cenário etc).

    Não tem imagem visual própria por padrão; serve só para testar colisão.
    Se quiser depurar visualmente, ative DEBUG_VISIVEL.
    """

    DEBUG_VISIVEL = True   # mude para True para ver os retângulos na tela

    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.rect = pygame.Rect(x, y, largura, altura)

        # Superfície só é usada se DEBUG_VISIVEL estiver ativo
        if self.DEBUG_VISIVEL:
            self.image = pygame.Surface((largura, altura), pygame.SRCALPHA)
            self.image.fill((255, 0, 0, 80))
        else:
            self.image = None

    def update(self, tela):
        if self.DEBUG_VISIVEL and self.image:
            tela.blit(self.image, self.rect)


def criar_grupo_obstaculos(lista_retangulos):
    grupo = pygame.sprite.Group()
    #percorre a lista e adiciona no grupo da seguinte forma
    
    for x, y, largura, altura in lista_retangulos:
        grupo.add(Obstaculo(x, y, largura, altura))

    return grupo