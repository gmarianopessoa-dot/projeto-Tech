# projeto-Tech
#Atividade Continuada 2 - AC (0,75)
#Instruções
#Desenvolver um sistema simples de controle bancário utilizando a linguagem Python. O programa deverá interagir com o usuário por meio do terminal, utilizando a função input() para exibir um menu de opções. O objetivo é exercitar conceitos fundamentais como variáveis, estruturas condicionais, estruturas de repetição e manipulação de strings.
#
#2.    DESCRIÇÃO DO PROBLEMA
#
#Crie um programa em Python que simule um sistema bancário com as seguintes funcionalidades:
#
#1 - Adicionar dinheiro (Depósito)
#2 - Sacar dinheiro
#3 - Mostrar extrato
#
#O sistema não deve permitir a realização de saques quando o saldo for insuficiente.
#
# 3.    ESTRUTURA DO MENU
#
#O programa deverá exibir o seguinte menu ao usuário:
#
#===== MENU =====
#1 - Adicionar Dinheiro
#2 - Sacar Dinheiro
#3 - Mostrar Extrato
#4 - Sair
#Escolha uma opção:
#
#4.    ESPECIFICAÇÃO DAS FUNÇÕES
#
#FUNÇÃO 1: ADICIONAR DINHEIRO
#
#Dados de Entrada:
#    •    Valor do depósito informado pelo usuário.
#
#Processamento Esperado:
#    •    Verificar se o valor é positivo.
#    •    Adicionar o valor ao saldo atual.
#    •    Registrar a operação no extrato.
#
#Dados de Saída:
#    •    Mensagem de confirmação do depósito.
#    •    Atualização do saldo.
#
#Exemplo de Saída:
#Depósito realizado com sucesso!
#Saldo atual: R$ 500.00
#
#FUNÇÃO 2: SACAR DINHEIRO
#
#Dados de Entrada:
#    •    Valor do saque informado pelo usuário.
#
#Processamento Esperado:
#    •    Verificar se o valor é positivo.
#    •    Conferir se há saldo suficiente.
#    •    Subtrair o valor do saldo.
##    •    Registrar a operação no extrato.
#    •    Impedir o saque em caso de saldo insuficiente.
#
#Dados de Saída:
#    •    Mensagem de confirmação ou erro.
#
#Exemplos de Saída:
#
#Saque realizado com sucesso!
#Saldo atual: R$ 300.00
#
#Ou:
#
#Saldo insuficiente para realizar o saque.
#
#FUNÇÃO 3: MOSTRAR EXTRATO

#Dados de Entrada:
#    •    Não há entrada direta do usuário além da escolha no menu.

#Processamento Esperado:
#    •    Exibir todas as operações realizadas.
#    •    Mostrar o saldo atual.

#Dados de Saída:

#===== EXTRATO =====
#Depósito: R$ 500.00
#Saque: R$ 200.00
#Saldo atual: R$ 300.00

#Caso não haja movimentações:

#===== EXTRATO =====
#Não foram realizadas movimentações.
#Saldo atual: R$ 0.00

#Envios de pasta
#Sem envios ainda. Arrastar e soltar para carregar sua atividade abaixo.

#Carregar Envio
##Deposite arquivos aqui ou clique abaixo!
#Você pode carregar arquivos de até um máximo de 2 GB.
#Comentários
#Comentários
saldo = 0
saldo = []
opicao = None
def AdicionarDInheiro(adicionar):
    if adicionar > 0:
        saldo.append(adicionar)
        print('Deposito realizado com Sucesso!')
        print(f'Saldo atual: R$ {sum(saldo):.2f}')
    else:
        print('Valor invalido para deposito. Por favor, insira um valor positivo.')
    return True

def SacarDinheiro ():
    saque = float(input('digite o valor pra sacar: '))
    if saque > 0 :
        saldo.append( - saque)
        print(' saque realizado com successo!')
        print(f'saldo atual: R$ {sum(saldo):.2f}')
    else: 
        print(' Nao possivel sacar esse valor')

def MostrarExtrato ():
    atual = sum(saldo)
    negativos = [n for n in saldo if n < 0]
    print(f'deposito:{negativos}')
    positivo = [s for s in saldo if s > 0]
    print(f'saldo: {positivo}')
    print(f'atual:{atual}')
    
while (opicao != '0'):
    print('===== MENU =====')
    print('1 - Adicionar Dinheiro')
    print('2 - Sacar Dinheiro')
    print('3 - Mostrar Extrato')
    print('4 - Sair')

    opicao = int(input('digite a opicao do menu: '))
    
    if opicao == 1:
        print()
        print('=====Adicionar Dinheiro=======')
        Dinheiro = float(input('digite o valor pra adicionar: '))
        AdicionarDInheiro(Dinheiro)
    elif opicao == 2:
        print()
        print('=====Sacar Dinheiro======')
        SacarDinheiro ()
    elif opicao == 3:
        print()
        print('=====Mostrar Extrato=====')
        MostrarExtrato()
        
    elif opicao == 4:
        break
    else:
        print('Opcao invalida')
