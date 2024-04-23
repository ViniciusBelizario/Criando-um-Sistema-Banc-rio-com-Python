"""
 Deve ser possivel depositar valores positivos para a minha conta bancaria. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos 
preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de 
extrato.

 O sistema deve permitir realizar 3 sques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir 
uma mensagem informando que não será possível sacar o dinhero por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação 
de extrato.

 Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem ser 
exibidos utilizando o formato R$ xxx.xx, exemplo:
    1500.45 = R$ 1500.45
"""

catalogo_de_opcoes = """
        QUAL OPÇÃO VOCÊ DESEJA?
    
    [d] Deposito
    [s] Sacar
    [e] Extrato
    [q] Sair

"""

saldo = 0
limite = 500
extrato = []
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    print(catalogo_de_opcoes)
    opcao = input("Qual operação deseja realizar: ")
    opcao.lower()

    if opcao == "d":
        valor_depositar = float(input("Quanto deseja depositar: "))
        if valor_depositar > 0:
            total = valor_depositar + saldo
            dado_extrato = f'{saldo} + {valor_depositar} = R$ {total}'
            extrato.append(dado_extrato)
            saldo = total
            print(f"Seu saldo é de: R${saldo}")

    elif opcao == "s":
        if numero_de_saques < LIMITE_DE_SAQUES:
            valor_sacar = float(input("Quanto deseja sacar: "))
            if valor_sacar <= limite:
                total = saldo - valor_sacar 
                dado_extrato = f"{saldo} - {valor_sacar} = R${total}"
                extrato.append(dado_extrato)
                saldo = total
                numero_de_saques += 1
                print("Operação realizada")
            else:
                print(f"Não é possivel sacar mais que {limite}")
        else:
            print("Você não pode mais sacar")

    elif opcao == "e":
        print("Seu extrato é de: ")
        for i in extrato:
            print(i)

    elif opcao == "q":
        print("Obrigado por realizar suas operações comigo até \nSeu extrato é de: ")
        break
