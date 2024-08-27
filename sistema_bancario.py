
import datetime as dt

def capturar_data_hora(data_e_hora):
    # Obter data e hora exata, e exibi-los em formato padrão do Brasil
    return dt.datetime.now().strftime(" [%d/%m/%y às %H:%M:%S] ")
    

def formatar_decimais(valor):
    # Formatar valores para exibir duas casas decimais 
    return f"R${valor:.2f}"


def sistema_bancario():
    menu = """

    [d] depositar
    [s] saque
    [e] extrato 
    [q] sair

    =>  """

    saldo = 0 
    valor_limite = 500 # Valor($$) limite para cada operação de saque
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3


    def depositar():
        nonlocal saldo
        valor = input("Informe o valor de depósito: ")
        try:
            valor = float(valor)

            if valor <= 0:
                print("Operação Inválida: O valor do depósito deve ser um número positivo maior que zero.\nPor favor, repita a operação com um valor válido.")
                return
            
            saldo += valor
            extrato.append(f"Deposito: {capturar_data_hora(valor)}+{formatar_decimais(valor)}\n")
            print(f"Deposito de {formatar_decimais(valor)} realizado com sucesso!")
            return
            
        except ValueError:
            print("Operação Inválida: Por favor, informe um valor numérico válido para o deposito.") 
            return None
        

    def sacar():
        nonlocal saldo
        nonlocal numero_saques
        valor = input("Informe o valor de saque: ")

        try:
            valor = float(valor)

            if valor <= 0:
                print("\bOperação Inválida: O valor de saque deve ser um número positivo maior que zero.\nPor favor, repita a operação com um valor válido.")
                return

            elif numero_saques >= LIMITE_SAQUES:
                print(f"Operação não realizada: Você atingiu o limite máximo({LIMITE_SAQUES}) de saques diários.\nPor favor, tente novamente amanhã.")
                return
            
            elif valor > saldo:
                print("Saldo insuficiente!")
                return       

            elif valor > valor_limite:
                print(f"Operação não realizada: O valor informado excede o limite máximo({formatar_decimais(valor_limite)}) de saque.\nPor favor, insira um valor dentro do limite.")
                return
            
            saldo -= valor
            numero_saques += 1
            extrato.append(f"Saque: {capturar_data_hora(valor)}-{formatar_decimais(valor)}\n")
            print(f"Saque de {formatar_decimais(valor)} realizado com sucesso!")
            return
            
        except ValueError: 
            print("Operação Inválida: Por favor, informe um valor numérico válido para o saque.")
            return None
        

    while True:

        opcao = input(menu)

        if opcao == "d":
            print("\nDeposito:\n")
            depositar()
                
        elif opcao == "s":
            print("\nSaque:\n")
            sacar()

        elif opcao == "e":
            print(f"\n======================== EXTRATO ========================\n")

            if extrato:
                print(f"  -  " + f"\n  -  ".join(extrato)+"\n=========================================================")

            else:
                print('Não foram realizadas movimentações nesta conta.\n=========================================================')

        elif opcao == "q":
            print("\nSaindo do Sistema...\n")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


sistema_bancario()
