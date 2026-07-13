import pygame
from animacoes.animacao_tela_inicial import Tela_inicial, Nome_jogo, Nuvens_tela_inicial,Botao_inicial_play,Botao_inicial_creditos,Botao_inicial_configuracoes
from animacoes.animacao_logo_etec import Creditos_inicial
#from animacoes.custcene import cutscene_embriao
from animacoes.tela_carregamento import Tela_de_carregamento
from ui.fade import Fade_in, Fade_out
from config.constantes import largura_tela, altura_tela,largura_pixel_tela,altura_pixel_tela,le_botoes,ale_botoes,largura_botoes,altura_botoes,le_menu,ale_menu
from animacoes.custcene import cutscene_embriao,Cutscene_olhos
from ui.menu import Menu,Botao_inicio,Botao_salvar,Botao_sair,Slider
from ui.creditos import Creditos_iniciais

# ── Animação inicial (logo Etec) ────────────────────────────────────────────
creditos = Creditos_inicial()

grupo_creditos = pygame.sprite.Group()
grupo_creditos.add(creditos)

# Fade-in branco que abre a cena do logo
grupo_fade_entrada = pygame.sprite.Group()
grupo_fade_entrada.add(Fade_in(largura_tela, altura_tela, (255, 255, 255)))

# Fade-out que encerra a cena do logo
grupo_fade_saida = pygame.sprite.Group()
grupo_fade_saida.add(Fade_out(largura_tela, altura_tela, (255, 255, 255)))

# ── Tela inicial ─────────────────────────────────────────────────────────────
grupo_tela_inicial = pygame.sprite.Group()
bg_tela_inicial=Tela_inicial()
nome_jogo=Nome_jogo()
grupo_tela_inicial.add(bg_tela_inicial)
grupo_tela_inicial.add(nome_jogo) 

#--------Menu---------------
menu_jogo=Menu(500,500,(le_menu,ale_menu),(largura_pixel_tela,altura_pixel_tela))
botaop_inicio=Botao_inicio(800,550,(0.20,0.20))
botaop_salvar=Botao_salvar(800,550,(0.20,0.20))
botaop_sair=Botao_sair(800,550,(0.20,0.20))
barra_musica=Slider((largura_pixel_tela//2)*0.62,(altura_pixel_tela//2)*0.45)

grupo_menu=pygame.sprite.Group()
grupo_menu.add(menu_jogo)
grupo_menu.add(botaop_inicio)
grupo_menu.add(botaop_salvar)
grupo_menu.add(botaop_sair)
grupo_menu.add(barra_musica)





#------Botões tela inicial----------------------------

grupo_botoes_menu=pygame.sprite.Group()
botao_play=Botao_inicial_play(largura_botoes,altura_botoes,(largura_pixel_tela,altura_pixel_tela),(le_botoes,ale_botoes))
botao_credito=Botao_inicial_creditos(largura_botoes,altura_botoes,(largura_pixel_tela,altura_pixel_tela),(le_botoes,ale_botoes))
botao_config=Botao_inicial_configuracoes(largura_botoes,altura_botoes,(largura_pixel_tela,altura_pixel_tela),(le_botoes,ale_botoes))
grupo_botoes_menu.add(botao_play)
grupo_botoes_menu.add(botao_credito)
grupo_botoes_menu.add(botao_config)

nuvens = Nuvens_tela_inicial()
#---------Tela de Carregamento-----------
tela_de_carregamento=Tela_de_carregamento(150,300,largura_tela,altura_tela)
grupo_tela_de_carregamento=pygame.sprite.Group()
grupo_tela_de_carregamento.add(tela_de_carregamento)

#---------Cutscene--------------------
Cutscene_sprite= cutscene_embriao(largura_tela,altura_tela)
grupo_cutscene = pygame.sprite.Group()
grupo_cutscene.add(Cutscene_sprite)

cutscene_Olho=Cutscene_olhos(largura_tela,altura_tela)
grupo_cOlhos=pygame.sprite.Group()
grupo_cOlhos.add(cutscene_Olho)

"--------Creditos-----------"
iniciar_creditos=Creditos_iniciais(500,500,(le_menu,ale_menu),(largura_pixel_tela,altura_pixel_tela))
grupo_creditos_pessoas=pygame.sprite.Group()
grupo_creditos_pessoas.add(iniciar_creditos)

