
class Conta:

    def __init__(self, saldo=int, nome=None, telefone=None):
        self.clientes = []
        self.saldo = saldo
        self.nome = nome
        self.telefone = telefone
    

    def printar_informacoes(self):
        print(f"Nome: {self.get.nome()}")
        print(f"Telefone: {self.get.telefone()}")
        print(f"Saldo: {self.get.saldo()}")
        print(f"Limite: {self.get.limite()}")

    def deposita(self, valor):
        print(valor)
        print(f"Saldo atual: {self.cliente.get.saldo()}")

    def saque(self, valor):
        if self.checa_saldo(valor):
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def cadastrar_cliente(self, saldo=int, nome=None, telefone=None):
        if nome is None:
            nome = input("Digite o nome do cliente: ").title()

        if telefone is None:
            telefone = input("Digite o telefone do cliente: ")
        
        tornar_vip = input("Deseja tornar o cliente VIP? (S/N): ").upper()
        if tornar_vip == "S":
            novo_cliente = ContaVip(numero=None, titular=None, saldo=0, limite=None, limite_extra=None)
            self.clientes.append(novo_cliente)
            return novo_cliente

        else:
            novo_cliente = Conta(0, nome, telefone)
            self.clientes.append(novo_cliente)
            
        while True:
            opcao = input('Conta criada com sucesso! Deseja fazer um depósito? (S/N): ').upper()
            if opcao == 'S':
                novo_cliente.deposita(int(input("Digite o valor do depósito: ")))
                print(f"Depósito realizado com sucesso! Saldo atual: {novo_cliente.get.saldo()}")
                Menu()
                break
            elif opcao == 'N':
                print('Operação cancelada!')
                Menu()
                break
            else:
                print("Opção inválida!")
    
class ContaVip(Conta):
    def __init__(self, numero, titular, saldo, limite, limite_extra):
        super().__init__(limite_extra)

        
    def limite_especial(self):
        return self.limite + self.limite_extra
    
    def printar_informacoes(self):
        print(f"Cliente: {self.titular}")
        print(f"Saldo: {self.saldo}")
        print(f"Limite: {self.limite}")
        print(f"Limite extra: {self.limite_extra}")

class ContaPoupanca(Conta):
    def __init__(self, saldo):
        super().__init__(saldo)
        # Rendimento de 0.5% ao mês
        self.taxa = 0.05

    def rendimento(self):
        return self.saldo * self.taxa


def Menu():
    print("1 - Criar conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato")
    print("5 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        Conta.cadastrar_cliente(self=None, saldo=int, nome=None, telefone=None)
    elif opcao == 2:
        Conta.deposita(self=None, valor=None)
    elif opcao == 3:
        Conta.saque(self=None, valor=None)
    elif opcao == 4:
        Conta.printar_informacoes(self=None)
    elif opcao == 5:
        exit()
    else:
        print("Opção inválida!")
        Menu()

Menu()
