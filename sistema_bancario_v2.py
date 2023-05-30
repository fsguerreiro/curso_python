

#argumentos de entrada: saldo, valor, extrato, limite, numero de saques, limite de saques
#argumentos de saída: saldo e extrato


def depositar(saldo, extrato):

    deposito = float(input('Informe o valor que deseja depositar na sua conta: '))
    saldo += deposito
    extrato.append(f"Depósito: R${deposito:.2f}")
    print("\nOperação de depósito realizada com sucesso!")
    #extrato.append(f"Saldo: R${saldo:.2f}")
    
    return saldo, extrato



def sacar(*, saldo, numero_saques, LIMITE_VALOR, LIMITE_SAQUES, extrato):
    
    if numero_saques >= LIMITE_SAQUES:
        print('\nErro: Voce não pode mais realizar saques hoje pois já ultrapassou o limite diário!')

    else:    
        valor_saque = float(input('Informe o valor que deseja sacar: '))

        if valor_saque <= LIMITE_VALOR:
                
            if valor_saque <= saldo:
                print('\nOperação realizada com sucesso! Imprimindo seu dinheiro...')
                saldo -= valor_saque
                extrato.append(f"Saque: R${valor_saque:.2f}")
                numero_saques += 1
                    
            else:
                print('\nErro: voce não tem saldo suficiente para essa sacar esta quantidade!')       

        else:
            print('\nErro: valor desejado é maior que o limite para cada saque!')
            
    #extrato.append(f"Saldo: R${saldo:.2f}")
    return saldo, extrato, numero_saques



def exibir_extrato(saldo, extrato):
    for item in extrato:
        print(item)

    print(f"Saldo: R${saldo:.2f}")



def cadastrar(usuarios, lista_cpf):
    
    cpf = input('Insira CPF: ')
    
    if cpf in lista_cpf:
        print("Erro! CPF já cadastrado.")
        return
    
    else:
 
        nome = input('Insira nome completo: ')
        data_nasc = input('Insira data de nascimento (DD/MM/AAAA): ')
        rua = input('Insira nome da rua/avenida: ')
        log = input('Insira numero da residência: ')
        bairro = input('Insira o bairro: ')
        cidade = input('Insira cidade/sigla do estado: ')
        cadastro = {'Nome': nome, 'Data de nascimento': data_nasc, 'no. CPF': cpf,
                'Endereço': {'Rua/Avenida': rua, 'Número': log, 'Bairro': bairro, 'Cidade/estado': cidade}}
        lista_cpf.append(cpf)
        usuarios.append(cadastro)
        
        return cadastro, lista_cpf, usuarios



def criar_conta(lista_conta, lista_cpf):
    agencia = '0001'

    while True:
        conta = input('Insira numero da conta (primeiro digito deve ser 1): ')
        if conta[0] == '1':

            if conta in lista_conta:
                print('Erro! Esta conta já pertence a um usuário')
                

            else:
                cpf_conta = input('Insira cpf: ')
                conta_reg = {'CPF': cpf_conta, 'conta': conta, 'agencia': agencia}
                lista_cpf.append(cpf_conta)
                lista_conta.append(conta)
                return conta_reg, lista_cpf, lista_conta
                break

        else:
            print('Voce inseriu o numero errado!')
    




saldo = 0
extrato = [f"Saldo inicial: R${saldo:.2f}"]
numero_saques = 0

lista_cpf = []
lista_conta = []
usuarios = []


menu = """
As seguintes opções estão disponíveis para operação:

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar usuário
[t] Cadastrar conta
[q] Sair
"""

while True:

    print(menu)
    opcao = input("Escolha uma das opções: ")
    
    if opcao == 'd':
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == 's':
        saldo, extrato, numero_saques = sacar(saldo = saldo, numero_saques = numero_saques, LIMITE_VALOR = 500, LIMITE_SAQUES = 3, extrato = extrato)

    elif opcao == 'e':
        exibir_extrato(saldo, extrato = extrato)

    elif opcao == 'c':
        usuario = cadastrar(usuarios, lista_cpf)

    elif opcao == 't':
        conta_reg, lista_cpf, lista_conta = criar_conta(lista_conta, lista_cpf)

    elif opcao == 'q':
        print("\nEncerrando sistema de atendimento, tenha um bom dia!")
        break

    else:
        print('\nEntrada inválida!')
