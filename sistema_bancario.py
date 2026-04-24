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