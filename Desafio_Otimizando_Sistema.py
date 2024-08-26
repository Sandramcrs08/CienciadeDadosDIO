# Função para saque
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para depósito
def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para extrato
def extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Lista de usuários (nome, data de nascimento, CPF, endereço)
usuarios = []

# Função para criar usuário
def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("CPF já cadastrado. Não é possível criar usuário.")
            return
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(f"Usuário {nome} criado com sucesso!")

# Lista de contas (agência, número da conta, usuário)
contas = []
numero_conta = 1

# Função para criar conta corrente
def criar_conta(usuario):
    global numero_conta
    agencia = "0001"
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    numero_conta += 1
    print(f"Conta criada para o usuário {usuario['nome']} - Agência: {agencia}, Número da Conta: {numero_conta-1}")

# Exemplo de uso:
saldo_inicial = 1000
limite = 500
extrato_inicial = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Criar Usuário
    [cc] Criar Conta
    [q] Sair
    => """
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo_inicial, extrato_inicial = deposito(saldo_inicial, valor, extrato_inicial)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo_inicial, extrato_inicial = saque(
            saldo=saldo_inicial,
            valor=valor,
            extrato=extrato_inicial,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )
    elif opcao == "e":
        extrato(saldo_inicial, extrato=extrato_inicial)
    elif opcao == "c":
        nome = input("Nome do usuário: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        criar_usuario(nome, data_nascimento, cpf, endereco)
    elif opcao == "cc":
        cpf = input("CPF do usuário para criar conta: ")
        usuario_encontrado = None