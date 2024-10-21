import datetime as dt
import pytz
import textwrap


# Função auxiliar para obter data e hora exata, e exibi-los em formato padrão do Brasil
def capturar_data_hora():
    data_utc = dt.datetime.now(pytz.timezone("America/Bahia"))
    return data_utc.strftime(" [%d/%m/%y às %H:%M:%S] ")


# Função auxiliar para formatar valores e exibi-los com duas casas decimais 
def formatar_decimais(valor): 
    return f"R${valor:.2f}"


def menu():
    menu_opcoes = """\n
    ======================== MENU ========================
    [d]\tDepositar
    [s]\tSaque
    [e]\tExtrato 
    [cc]\tCadastrar cliente
    [nc]\tNova conta
    [lc]\tListar contas
    [q]\tSair

    =>  """

    return input(textwrap.dedent(menu_opcoes))


def depositar(saldo, extrato, numero_transacoes, LIMITE_TRANSACOES):
    try:
        valor = float(input("Informe o valor de depósito: "))

        if valor <= 0:
            print("\n@@@  Operação Inválida: O valor do depósito deve ser um número positivo maior que zero.\nPor favor, repita a operação com um valor válido.  @@@")
            return saldo, extrato, numero_transacoes  
             
        elif numero_transacoes >= LIMITE_TRANSACOES:
            print(f"\n@@@  Operação não realizada: Você atingiu o limite máximo({LIMITE_TRANSACOES}) de transações diárias.\nPor favor, tente novamente amanhã.  @@@")
            return saldo, extrato, numero_transacoes
        
        else:
            saldo += valor
            numero_transacoes += 1
            extrato.append(f"Depósito: {capturar_data_hora()} + {formatar_decimais(valor)}")
            print(f"\n☰☰☰  Depósito de {formatar_decimais(valor)} realizado com sucesso!  ☰☰☰\n")
            
            return saldo, extrato, numero_transacoes
        
    except ValueError:
        print("\n@@@  Operação Inválida: Por favor, informe um valor numérico válido para o depósito.  @@@") 
        return saldo, extrato, numero_transacoes
    

def sacar(saldo, extrato, valor_limite_saque, numero_transacoes, limite_transacoes):
    try:
        valor = float(input("Informe o valor de saque: "))

        if valor <= 0:
            print("\n@@@  Operação Inválida: O valor de saque deve ser um número positivo maior que zero.\nPor favor, repita a operação com um valor válido.  @@@")
            return saldo, extrato, numero_transacoes
        
        elif numero_transacoes >= limite_transacoes:
            print(f"\n@@@  Operação não realizada: Você atingiu o limite máximo({limite_transacoes}) de transações diárias.\nPor favor, tente novamente amanhã.  @@@")
            return saldo, extrato, numero_transacoes   
             
        elif valor > saldo:
            print("\n@@@  Saldo insuficiente!  @@@")
            return saldo, extrato, numero_transacoes  
             
        elif valor > valor_limite_saque:
            print(f"\n@@@  Operação não realizada: O valor informado excede o limite máximo({formatar_decimais(valor_limite_saque)}) de saque.\nPor favor, insira um valor dentro do limite.  @@@")
            return saldo, extrato, numero_transacoes    
            
        else:
            saldo -= valor
            numero_transacoes += 1
            extrato.append(f"Saque: {capturar_data_hora()} - {formatar_decimais(valor)}")
            print(f"\n☰☰☰  Saque de {formatar_decimais(valor)} realizado com sucesso!  ☰☰☰\n")
            
            return saldo, extrato, numero_transacoes
        
    except ValueError: 
        print("\n@@@  Operação Inválida: Por favor, informe um valor numérico válido para o saque.  @@@")
        return saldo, extrato, numero_transacoes
    

def exibir_extrato(saldo, extrato):
    print(f"\n======================== EXTRATO ========================\n")

    if extrato:
        print("\n  -  " + "\n  -  ".join(extrato))
        print(f"\n - SALDO:\t\t{formatar_decimais(saldo)} ")
    else:
        print('   Não foram realizadas movimentações nesta conta.\n')
    
    print("=========================================================")


def cadastrar_cliente(clientes):
    try:
        cpf = input("Informe seu CPF (somente números): ").strip()

        # Verifica se já existe cliente com o CPF fornecido
        if filtrar_cliente(cpf, clientes):
            print("\n@@@  Já existe usuário com esse CPF! @@@\n")
            return

        # Verifica se o CPF foi informado
        if not cpf:
            print("\n@@@  Operação Inválida: O CPF não pode ser vazio. @@@")
            return

        # Captura e valida o nome do cliente
        nome = input("Informe o seu nome: ").strip()
        if not nome:
            print("\n@@@  Operação Inválida: O nome não pode ser vazio. @@@")
            return      
        elif not nome.replace(" ", "").isalpha():
            print("\n@@@  Operação Inválida: Por favor, informe um nome válido (somente letras são permitidas). @@@")
            return 

        # Captura outras informações do cliente
        data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o seu endereço (logradouro, N° - bairro - cidade/sigla estado): ")

        # Adiciona o novo cliente à lista
        novo_cliente = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco
        }
        clientes.append(novo_cliente)
        print("\n☰☰☰  Cliente cadastrado com sucesso!  ☰☰☰\n")

        return novo_cliente 
    
    except Exception as err:
        print("\n@@@  Cliente NÃO cadastrado: Um erro inesperado ocorreu. Por favor, tente novamente mais tarde.  @@@")
        print("@@@  Detalhes do erro:", err, "  @@@")
        return None


# Função auxiliar para filtrar clientes por CPF
def filtrar_cliente(cpf, clientes):
    # Verifica se já existe um cliente com o CPF fornecido. Se existir, retorna cliente.
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None
  

def criar_conta(agencia, numero_conta, clientes):
    try:
        cpf = input("Informe o CPF do cliente: ")
        cliente = filtrar_cliente(cpf, clientes)

        if cliente:
            nova_conta = {
                "agencia": agencia,
                "numero_conta": numero_conta,
                "cliente": cliente
            }
            print("\n☰☰☰  Conta criada com sucesso!  ☰☰☰\n")
            return nova_conta
        else:
            print("\n@@@  Cliente não encontrado, fluxo de criação de conta encerrado!  @@@")
            return None

    except Exception as err:
        print("\n@@@  A conta NÃO foi criada: Um erro inesperado ocorreu. Por favor, tente novamente mais tarde.  @@@")
        print("@@@  Detalhes do erro:", err, "  @@@")
        return None


def listar_contas(contas):
    if not contas:
        print("\n@@@  Não existem contas cadastradas.  @@@\n")
        return
    
    for indice, conta in enumerate(contas):
        exibir_conta = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}              
        """
        print("=" * 100)
        print(textwrap.dedent(exibir_conta))


# Função principal
def sistema_bancario():
    LIMITE_TRANSACOES = 10
    VALOR_LIMITE_SAQUE = 500  # Valor limite para cada operação de saque
    AGENCIA = "0001"

    saldo = 0 
    extrato = []
    numero_transacoes = 0
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            print("\nDepósito:\n")
            saldo, extrato, numero_transacoes = depositar(saldo, extrato, numero_transacoes, LIMITE_TRANSACOES)
                
        elif opcao == "s":
            print("\nSaque:\n")
            saldo, extrato, numero_transacoes = sacar(saldo, extrato, VALOR_LIMITE_SAQUE, numero_transacoes, LIMITE_TRANSACOES)
                
        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "cc":
            print("\nCadastro de cliente:\n")
            cadastrar_cliente(clientes)

        elif opcao == "nc":
            print("\nNova conta:\n")
            conta = criar_conta(AGENCIA, len(contas) + 1, clientes)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            print("\nListar contas:\n")
            listar_contas(contas)

        elif opcao == "q":
            print("\n☰☰☰  Até logo! ☰☰☰\n")
            break

        else:
            print("\n@@@  Opção inválida!  @@@\n")


# Chama a função principal
if __name__ == "__main__":
    sistema_bancario()
