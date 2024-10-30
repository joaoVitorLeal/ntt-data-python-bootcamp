import datetime as dt
import pytz
import textwrap
from abc import ABC, abstractmethod

# Função auxiliar para obter data e hora exata, e exibi-los em formato padrão do Brasil
def capturar_data_hora():
    data_utc = dt.datetime.now(pytz.timezone("America/Bahia"))
    return data_utc.strftime(" [%d/%m/%y às %H:%M:%S] ")


# Função auxiliar para formatar valores e exibi-los com duas casas decimais 
def formatar_decimais(valor): 
    return f"R${valor:.2f}"


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self._cpf = cpf


class Conta:
    def __init__(self, numero_conta, cliente):
        self._saldo = 0
        self._numero_conta = numero_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero_conta):
        return cls(numero_conta, cliente)
    
    # getters #
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@  Saldo insuficiente!  @@@")
        elif valor > 0:
            print(f"\n☰☰☰  Saque de {formatar_decimais(valor)} realizado com sucesso!  ☰☰☰\n")
            self._saldo -= valor
            return True
        else:
            print("\n@@@  Operação falhou! O valor informado é inválido.  @@@")
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\n☰☰☰  Depósito de {formatar_decimais(valor)} realizado com sucesso!  ☰☰☰\n")
        else:
            print("\n@@@  Operação falhou! O valor informado é inválido.  @@@")
            return False
        
        return True


class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite_transacoes=10, valor_limite_saque=500):
        super().__init__(numero_conta, cliente)
        self.limite_transacoes = limite_transacoes
        self.valor_limite_saque = valor_limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["Tipo"] == Saque.__name__]
        )

        excedeu_limite_saque = valor > self.valor_limite_saque
        excedeu_qnt_transacoes = numero_saques >= self.limite_transacoes

        if excedeu_limite_saque:
            print(f"\n@@@  Operação não realizada: O valor informado excede o limite máximo ({formatar_decimais(self.valor_limite_saque)}) de saque.\nPor favor, insira um valor dentro do limite.  @@@")
        elif excedeu_qnt_transacoes:
            print(f"\n@@@  Operação não realizada: Você atingiu o limite máximo ({self.limite_transacoes}) de transações diárias.\nPor favor, tente novamente amanhã.  @@@")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self._agencia}
            C/C:\t{self._numero_conta}
            Titular:\t{self._cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "Tipo": transacao.__class__.__name__,
                "Valor": transacao.valor,
                "Data": capturar_data_hora()
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


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


# Função auxiliar para filtrar clientes por CPF
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente._cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@\n")
        return
    
    # FIXME: Não permite cliente escolher a conta
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@  Cliente não encontrado! @@@\n")
        return

    valor = float(input("Informe o valor de depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
    

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@  Cliente não encontrado! @@@\n")
        return

    valor = float(input("Informe o valor de saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
    

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@  Cliente não encontrado! @@@\n")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return    
    
    print(f"\n======================== EXTRATO ========================\n")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        print('   Não foram realizadas movimentações nesta conta.\n')

    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['Tipo']}:\n\t{formatar_decimais(transacao['Valor'])}"
    
    print(extrato)
    print(f"\nSaldo:\n\t{formatar_decimais(conta.saldo)}")
    print(f"\n=========================================================\n")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@  Já existe cliente com esse CPF! @@@\n")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print("\n☰☰☰  Cliente cadastrado com sucesso!  ☰☰☰\n")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@  Cliente não encontrado, fluxo de criação de conta encerrado!  @@@\n")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero_conta=numero_conta)
    cliente.adicionar_conta(conta)
    contas.append(conta)

    print("\n☰☰☰  Conta criada com sucesso!  ☰☰☰\n")


def listar_contas(contas):
    print("\n==================== CONTAS =====================\n")
    
    if not contas:
        print('   Nenhuma conta cadastrada.\n')
    
    else:
        for conta in contas:
            print(f"{conta}")

    print("\n================================================\n")


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "cc":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@  Operação inválida, por favor selecione novamente a operação desejada.  @@@")


if __name__ == "__main__":
    main()
