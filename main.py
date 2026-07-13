import os
import sys

os.environ["SDL_VIDEO_CENTERED"] = "1"

import pygame
from pygame.locals import *

# ── Inicialização ─────────────────────────────────────────────────────────────
pygame.init()

# config_janela cria a janela; importar depois do pygame.init()
from config.constantes import fps, tela
from config.config_janela import mudar_tamanho_tela
from telas.estados import atualizar_estado,carregar_ui
from grupos.grupos_sprite import botao_play,tela_de_carregamento,botao_config,menu_jogo,botaop_inicio,botaop_sair,botao_credito,iniciar_creditos,barra_musica

# ── Loop principal ────────────────────────────────────────────────────────────
rodando = True

while rodando:

    # 1. Processar eventos — NENHUMA lógica de jogo aqui
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
        if event.type == KEYDOWN:
            if event.key == K_F11:
                mudar_tamanho_tela()
            if event.key == K_ESCAPE:
                rodando = False
        botao_play.verificar_play(event)
        botao_config.verificar_config(event)
        tela_de_carregamento.verificar_click_porta(event)
        menu_jogo.vexit_menu(event)
        botaop_inicio.click_inicio(event)
        botao_credito.click_creditos(event)
        iniciar_creditos.verificar_click(event)
        barra_musica.evento(event)
        if menu_jogo.menu_aberto:
            botaop_inicio.click_inicio(event)
            if botaop_sair.click_sair(event):
                rodando=False
        


    # 2. Atualizar + desenhar o estado atual
    atualizar_estado()
    carregar_ui()
    

    # 3. Apresentar o frame na tela
    pygame.display.flip()

    # 4. Controlar FPS — 60 quadros por segundo
    fps.tick(60)

# ── Encerramento ──────────────────────────────────────────────────────────────

pygame.quit()
sys.exit()


# ── Utilitário para empacotamento com PyInstaller ─────────────────────────────
def caminho_recurso(caminho):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, caminho)
