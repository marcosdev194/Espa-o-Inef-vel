import pygame
from telas.carregar_animacoes import carregar_logo_etec, carregar_tela_inicial,Carregamento,Cutscene,carregar_menu,carregar_creditoi,Carregar_Cutscene_olhos
from grupos.grupos_sprite import botaop_inicio,botao_config,botao_credito
from telas.carregar_mapas import Carregar_quarto,Carregar_corredor_casa
# Estado inicial do jogo
estado_atual = 'animacao_inicial'
ui_atual=None
funcao_atual=None

# Mapa de estado → função de renderização
# Cada função é chamada a cada frame e retorna True quando quer trocar de estado
ESTADOS_COM_UI_PERMITIDA = {'tela_inicial'}
lista_estados = {
    'animacao_inicial': carregar_logo_etec,
    'tela_inicial':     carregar_tela_inicial,
    'carregamento':         Carregamento,
    'cutscene_embriao':             Cutscene,
    'quarto_caleb':         Carregar_quarto,
    'cutscene_olhos':       Carregar_Cutscene_olhos,
    'corredor_casa':        Carregar_corredor_casa
}

# Sequência de transição entre estados
proximos_estados = {
    'animacao_inicial': 'tela_inicial',
    'tela_inicial':     'carregamento', 
    'carregamento':     'cutscene_embriao',
    'cutscene_embriao':  'cutscene_olhos',
    'cutscene_olhos':     'quarto_caleb',
    'quarto_caleb':        'corredor_casa'
}

lista_ui={
    'menu':   carregar_menu,
    'creditos': carregar_creditoi 
}
retorno_FUi=[carregar_menu,carregar_creditoi]
"""listan_ui=(
    
    'menu',
    'creditos'
)"""

def atualizar_estado():
    """
    Chama a função do estado atual. Se ela retornar True,
    avança para o próximo estado automaticamente.
    """
    global estado_atual
    funcao = lista_estados[estado_atual]
    trocar = funcao()
    if botaop_inicio.clicado_inicio:
        estado_atual='tela_inicial'
    if trocar and estado_atual in proximos_estados:
        proximo = proximos_estados[estado_atual]
        if proximo != estado_atual:
            # Saindo da tela_inicial: zera flags de botões para não "vazar"
            # cliques pendentes para o próximo estado (causa do seu bug)
            if estado_atual == 'tela_inicial':
                botao_config.foi_clicado     = False
                botao_credito.clicado_creditos = False
            estado_atual = proximo
 
 
def carregar_ui():
    global ui_atual
 
    # ── Bloqueio por estado: a causa do seu bug ──────────────────────────────
    # Se o estado atual não é um dos que permite UI, não roda nada daqui.
    # Isso impede que menu/créditos apareçam durante carregamento ou cutscene,
    # mesmo que as flags de clique tenham ficado "pendentes" de outro estado.
    if estado_atual not in ESTADOS_COM_UI_PERMITIDA:
        ui_atual = None   # garante que nada fica "preso" aberto entre estados
        return
 
    if ui_atual is None:
        for nome, funcao in lista_ui.items():
            resultado = funcao()
            if resultado:
                ui_atual = nome
                break
 
    else:
        funcao = lista_ui[ui_atual]
        resultado = funcao()
        if not resultado:
            ui_atual = None