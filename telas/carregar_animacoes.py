import pygame
from config.constantes import tela
from grupos.grupos_sprite import (
    grupo_creditos, grupo_fade_entrada, grupo_fade_saida,grupo_botoes_menu,
    grupo_tela_inicial, nuvens, creditos,botao_play,bg_tela_inicial,nome_jogo,grupo_tela_de_carregamento,
    botao_config,botao_credito,grupo_cutscene,
    tela_de_carregamento,Cutscene_sprite,menu_jogo,grupo_menu,grupo_creditos_pessoas,iniciar_creditos,grupo_cOlhos,cutscene_Olho
)
DEBUG_HITBOX=True

def carregar_logo_etec():
    """
    Chamada a cada frame enquanto estado == 'animacao_inicial'.
    Retorna True quando a animação terminar (sinaliza troca de estado).
    """
    # 1. Limpa a tela com branco (fundo da cena do logo)
    tela.fill((255, 255, 255))

    # 2. Fade-in branco sobre tudo no início
    if not grupo_fade_entrada.sprites()[0].concluido:
        grupo_fade_entrada.update(tela)

    # 3. Logo + texto com fade
    grupo_creditos.update(tela)

    # 4. Quando o logo saiu, faz o fade-out final
    if creditos.concluido:
        grupo_fade_saida.update(tela)
        if grupo_fade_saida.sprites()[0].concluido:
            return True   # ← sinaliza: pode trocar de estado


    



    return False


def carregar_tela_inicial():
    """Chamada a cada frame enquanto estado == 'tela_inicial'."""

    if botao_play.foi_clicado:
        bg_tela_inicial.iniciar_saida()
        nome_jogo.iniciar_saida()


        if bg_tela_inicial.concluido:
            return True

    grupo_tela_inicial.update(tela)
    nuvens.Mover_nuvens()
    nuvens.Desenhar_nuvens(tela)
    grupo_botoes_menu.update(tela)

    if not botao_play.foi_clicado:
        grupo_botoes_menu.update(tela)

    if DEBUG_HITBOX:
            # Borda colorida em cima de cada botão
            pygame.draw.rect(tela, (255, 0,   0),  botao_play.rect,          2)  # vermelho
            pygame.draw.rect(tela, (0,   255, 0),  botao_config.rect, 2)  # verde
            pygame.draw.rect(tela, (0,   0,   255), botao_credito.rect,     2)  # azul
    
            # Posição do mouse + rect do play no canto da tela
            fonte_debug = pygame.font.SysFont("Arial", 18)
            pos = pygame.mouse.get_pos()
            txt = fonte_debug.render(
                f"Mouse: {pos}    Play rect: {botao_play.rect}",
                True, (255, 255, 0)
            )
            tela.blit(txt, (10, 10))
    if bg_tela_inicial.concluido:
        return True
    return False


def Carregamento():
    grupo_tela_de_carregamento.update(tela)
    if tela_de_carregamento.concluido:
        global acabou_carre
        acabou_carre=pygame.time.get_ticks()
        return True
    return False
def Cutscene():
    
    if Cutscene_sprite.concluido:
        return True
    if pygame.time.get_ticks()-acabou_carre>=2000:
        grupo_cutscene.update(tela)
    return False  

def Carregar_Cutscene_olhos():
    if Cutscene_sprite.concluido:
        grupo_cOlhos.update(tela)
        if cutscene_Olho.concluido:
            return True
        return False
        


def carregar_menu():
    if botao_config.foi_clicado:
        menu_jogo.menu_aberto=True
    if menu_jogo.exit_clicado:
        menu_jogo.menu_aberto=False
        menu_jogo.exit_clicado=False
        botao_config.foi_clicado=False
        return False
    elif menu_jogo.menu_aberto:
        grupo_menu.update(tela)
        return True
    return False

def carregar_creditoi():
    if botao_credito.clicado_creditos:
        iniciar_creditos.creditos_aberto=True
    if iniciar_creditos.exit_clicado:
        iniciar_creditos.creditos_aberto=False
        iniciar_creditos.exit_clicado=False
        botao_credito.clicado_creditos=False
        return False
    elif iniciar_creditos.creditos_aberto:
        grupo_creditos_pessoas.update(tela)
        return True
    return False

