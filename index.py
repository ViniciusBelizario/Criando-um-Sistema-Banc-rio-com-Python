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



""""
  Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

  Precisamnos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacara, depositar e visualizar histórico.
Além disso. para a verão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente 
(vincular com usuário).

  Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada funçãp vai ter uma regra na passagem de 
argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.

  A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
Sugestão de retorno:
    saldo e extrato.

  A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato.
Sugestão de retorno:    
    saldo e extrando

  A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). 
Argumentos posicionais: saldo
Argumento nomeados: extrato.

  Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a contade para adicionar mais funções.
Exemplo:
    listar contas

  O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro,
número - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

  O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agêndia 
é fixo: '001'. O Usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

  Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF indormado para cada usuário da lista

"""
usuarios = []
contas = []
operacoes = []
saldo = 0

def depositar(valor, saldo):
    if valor > 0:
        saldo += valor
        return saldo, f"Depósito de R$ {valor:.2f}"
    else:
        print("Erro: Valor de depósito deve ser positivo.")
        return saldo, None
    
def sacar(*, saldo, valor, extrato, limite_saque, numero_saques, limite_diario):
    if numero_saques < limite_diario and valor <= limite_saque:
        if saldo >= valor:
            saldo -= valor
            return saldo, f"Saque de R$ {valor:.2f}"
        else:
            print("Erro: Saldo insuficiente.")
    else:
        print("Erro: Limite de saques diários alcançado ou valor além do limite.")
    return saldo, None

def extrato(saldo, *, operacoes):
    print("Extrato de operações:")
    for operacao in operacoes:
        print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}")

def criar_usuario(nome, data_nascimento, cpf, endereco):
    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    return novo_usuario

def criar_conta(usuario, contas):
    nova_conta = {
        'agencia': '001',
        'numero_conta': len(contas) + 1,
        'usuario': usuario
    }
    contas.append(nova_conta)
    return nova_conta

def menu():
    print("\nBem-vindo ao Banco Simplificado!")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Criar usuário")
    print("5. Criar conta bancária")
    print("6. Sair")
    return input("Escolha uma opção: ")

def main():
    global saldo
    numero_de_saques = 0
    while True:
        opcao = menu()
        if opcao == '1':  # Depósito
            valor = float(input("Informe o valor do depósito: "))
            saldo_atualizado, descricao = depositar(valor, saldo)
            if descricao:
                operacoes.append(descricao)
                saldo =saldo_atualizado
                print(f"Depósito realizado. Saldo atual: R$ {saldo_atualizado:.2f}")
        elif opcao == '2':  # Saque
            if numero_de_saques < 3:
                valor = float(input("Informe o valor do saque: "))
                saldo_atualizado, descricao = sacar(saldo=saldo, valor=valor, extrato=operacoes, limite_saque=500, numero_saques=numero_de_saques, limite_diario=3)
                if descricao:
                    numero_de_saques += 1
                    saldo =saldo_atualizado
                    operacoes.append(descricao)
                    
                    print(f"Saque realizado. Saldo atual: R$ {saldo_atualizado:.2f}")
                else:
                    print("Saque não realizado.")
            else:
                print("Limite de saques diários alcançado.")
        elif opcao == '3':  # Extrato
            extrato(saldo, operacoes=operacoes)
        elif opcao == '4':  # Criar usuário
            nome = input("Nome do usuário: ")
            data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço completo: ")
            usuario = criar_usuario(nome, data_nascimento, cpf, endereco)
            usuarios.append(usuario)
            print("Usuário criado com sucesso.")
        elif opcao == '5':  # Criar conta
            cpf = input("CPF do usuário para a nova conta: ")
            usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
            if usuario:
                conta = criar_conta(usuario, contas)
                print(f"Conta criada com sucesso. Número da conta: {conta['numero_conta']}")
            else:
                print("Usuário não encontrado.")
        elif opcao == '6':  # Sair
            print("Obrigado por usar o Banco Simplificado.")
            break
        else:
            print("Opção inválida, por favor tente novamente.")

if __name__ == '__main__':
    main()