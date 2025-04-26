import os

# ==============================================================================
# Funcoes extras

def limpar():
    os.system('cls')

def nome_caixa():
    print('SUPER EXPRESS MARKET\nCAIXA DE AUTO-ATENDIMENTO\n')

# ==============================================================================

# ==============================================================================
# Area de cadastro de itens.

def opcao_invalida_escolha_cadastro():
    print('\nOpcao invalida.')
    input('\nPressione "Enter" para tentar novamente. ')
    senha_incorreta_cadastro()

def senha_incorreta_cadastro():
    limpar()
    nome_caixa()
    print('Senha incorreta\n')
    print('1. Tentar novamente')
    print('2. Voltar ao menu principal\n')

    try:
        senha_incorreta_cadastro_escolha = int(input('Escolha uma opcao: '))

        if senha_incorreta_cadastro_escolha == 1:
            bloqueio_cadastro()
        elif senha_incorreta_cadastro_escolha == 2:
            menu_principal()
        else:
            opcao_invalida_escolha_cadastro()
    except ValueError:
        opcao_invalida_escolha_cadastro()

def cadastro_item_desbloqueado():
    limpar()
    nome_caixa()
    pass

def bloqueio_cadastro():
    limpar()
    nome_caixa()
    print('Acesso restrito a somente pessoas autorizadas.\n')
    senha = input('Digite a senha: ')

    if senha == 'admin123':
        cadastro_item_desbloqueado()
    else:
        senha_incorreta_cadastro()

# ==============================================================================

# ==============================================================================
# Area de atividade de itens.

def opcao_invalida_escolha_atividade():
    print('\nOpcao invalida.')
    input('\nPressione "Enter" para tentar novamente. ')
    senha_incorreta_atividade()

def senha_incorreta_atividade():
    limpar()
    nome_caixa()
    print('Senha incorreta\n')
    print('1. Tentar novamente')
    print('2. Voltar ao menu principal\n')

    try:
        senha_incorreta_atividade_escolha = int(input('Escolha uma opcao: '))

        if senha_incorreta_atividade_escolha == 1:
            bloqueio_cadastro()
        elif senha_incorreta_atividade_escolha == 2:
            menu_principal()
        else:
            opcao_invalida_escolha_atividade()
    except ValueError:
        opcao_invalida_escolha_atividade()

def atividade_item_desbloqueado():
    limpar()
    nome_caixa()
    pass

def bloqueio_atividade():
    limpar()
    nome_caixa()
    print('Acesso restrito a somente pessoas autorizadas.\n')
    senha = input('Digite a senha: ')

    if senha == 'admin123':
        atividade_item_desbloqueado()
    else:
        senha_incorreta_atividade()

# ==============================================================================

# ==============================================================================
# Area de opcoes do menu inicial.

def exibir_opcoes():
    limpar()
    nome_caixa()
    print('1. Realizar compra e pagamento')
    print('2. Cadastrar novo item')
    print('3. Ativar/Desativar item')
    print('4. Cancelar e sair\n')

def compra():
    limpar()
    nome_caixa()
    pass

def sair():
    limpar()
    nome_caixa()
    print('Saindo...')
    input('\nPressione "Enter" para iniciar novamente.')
    tela_inicial()

def opcao_invalida():
    print('\nOpcao invalida.')
    input('\nPressione "Enter" para tentar novamente. ')
    menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))

        if opcao_escolhida == 1:
            compra()
        elif opcao_escolhida == 2:
            bloqueio_cadastro()
        elif opcao_escolhida == 3:
            bloqueio_atividade()
        elif opcao_escolhida == 4:
            sair()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

# ==============================================================================

def menu_principal():
    limpar()
    nome_caixa()
    exibir_opcoes()
    escolher_opcao()

def tela_inicial():
    limpar()
    nome_caixa()
    print('Ola! Seja bem-vindo ao caixa de auto-atendimento Super Express Market.')
    input('\nPressione "Enter" para iniciar.')
    menu_principal()

# ==============================================================================

tela_inicial()