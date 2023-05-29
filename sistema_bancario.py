menu = """
As seguintes opções estão disponíveis para operação:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    print(menu)
    opcao = input("Escolha uma das opções: ")

    if opcao == 'd':
        deposito = float(input('Informe o valor que deseja depositar na sua conta: '))
        saldo += deposito
        extrato.append(f"Depósito: R${deposito:.2f}")
        print("\nOperação de depósito realizada com sucesso!")


    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print('\nErro: Voce não pode mais realizar saques hoje pois já ultrapassou o limite diário!')

        else:    
            valor_saque = float(input('Informe o valor que deseja sacar: '))

            if valor_saque <= limite:
                
                if valor_saque <= saldo:
                    print('\nOperação realizada com sucesso! Imprimindo seu dinheiro...')
                    saldo -= valor_saque
                    extrato.append(f"Saque: R${valor_saque:.2f}")
                    numero_saques += 1
                    
                else:
                    print('\nErro: voce não tem saldo suficiente para essa sacar esta quantidade!')

            else:
                print('\nErro: valor desejado é maior que o limite para cada saque!')


    elif opcao == 'e':
        
        for op in extrato:
            print(op)

        print(f"Saldo: R${saldo:.2f}")

    
    elif opcao == 'q':
        print("\nEncerrando sistema de atendimento, tenha um bom dia!")
        break


    else:
        print('\nEntrada inválida!')
