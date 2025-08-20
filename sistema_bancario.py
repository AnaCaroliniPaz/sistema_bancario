# sistema_bancario_sem_transferencia.py

class Usuario:
    def __init__(self, nome, nascimento, cpf, endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereco = endereco


class Conta:
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500.0

    def __init__(self, usuario, numero):
        self.usuario = usuario
        self.numero = numero
        self.saldo = 0.0
        self.saques_realizados = 0
        self.extrato = []

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser maior que zero.")
            return
        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if self.saques_realizados >= Conta.LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários.")
            return
        if valor > Conta.LIMITE_VALOR_SAQUE:
            print(f"O valor máximo por saque é R$ {Conta.LIMITE_VALOR_SAQUE:.2f}.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para saque.")
            return

        self.saldo -= valor
        self.saques_realizados += 1
        self.extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def emitir_extrato(self):
        print(f"\n=== Extrato da Conta {self.numero} ===")
        if not self.extrato:
            print("Nenhuma operação realizada.")
        else:
            for operacao in self.extrato:
                print(operacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("==============================\n")


# Banco e cadastro
usuarios = []
contas = []

def cadastrar_usuario(nome, nascimento, cpf, endereco):
    if any(u.cpf == cpf for u in usuarios):
        print("CPF já cadastrado. Cadastro não realizado.")
        return None
    usuario = Usuario(nome, nascimento, cpf, endereco)
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")
    return usuario

def criar_conta(usuario):
    numero_conta = f"0001-{len(contas)+1:04d}"
    conta = Conta(usuario, numero_conta)
    contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    return conta


# Menu principal
def main():
    print("=== Bem-vindo ao Sistema Bancário da Ana Carolini! ===")
    
    nome = input("Nome: ")
    nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")

    usuario = cadastrar_usuario(nome, nascimento, cpf, endereco)
    if not usuario:
        return

    conta = criar_conta(usuario)

    while True:
        print("\nEscolha uma operação:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Emitir extrato")
        print("4 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            valor = float(input("Valor do depósito: R$ "))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Valor do saque: R$ "))
            conta.sacar(valor)
        elif opcao == "3":
            conta.emitir_extrato()
        elif opcao == "4":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
