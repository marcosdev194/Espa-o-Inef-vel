import pygame


def tempo_agora():
    """Retorna o tempo em ms desde que o pygame foi iniciado."""
    return pygame.time.get_ticks()


def tempo_passou(tempo_inicio, duracao_ms):
    """Retorna True se 'duracao_ms' milissegundos já passaram desde 'tempo_inicio'."""
    return pygame.time.get_ticks() - tempo_inicio >= duracao_ms
