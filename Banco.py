from Conta import Conta, ContaBonus, ContaPoupanca

class Banco:
    def __init__(self):
        self.contas = {}

    def cadastrar_conta(self, numero, tipo='simples'):
        if numero in self.contas:
            print("Conta já existe!")
            return False

        if tipo == "bonus":
            self.contas[numero] = ContaBonus(numero)
        
        elif tipo == "poupanca":
            self.contas[numero] = ContaPoupanca(numero)
            # Exigindo saldo inicial rel- 1.3
            valor_inicial = float(input("Qual o saldo inicial da conta? "))
            self.contas[numero].saldo = valor_inicial
        
        else:
            self.contas[numero] = Conta(numero)


        print(f"Conta {numero} ({tipo.capitalize()}) cadastrada com sucesso.")
        return True

    def ver_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada.")
        
        for conta in self.contas.values():
            print(conta)

    def consultar_saldo(self, numero):
        conta = self.contas.get(numero)
        if not conta:
            print("Conta não encontrada!")
            return None
        print(f"Saldo da conta {numero}: R${conta.saldo:.2f}")
        return conta.saldo

    def credito(self, numero, valor):
        conta = self.contas.get(numero)

        if not conta:
            print("Conta não encontrada!")
            return False
        
        # Garatindo que o valor seja positivo
        if valor <= 0:
            print("Valor de crédito deve ser positivo!")
            return False

        conta.saldo += valor
        if isinstance(conta, ContaBonus):
            conta.adicionar_pontos_deposito(valor)

        print(f"Crédito de R${valor:.2f} realizado na conta {numero}.")
        return True

    def debito(self, numero, valor):
        conta = self.contas.get(numero)
        
        if not conta:
            print("Conta não encontrada!")
            return False

        # Garatindo que o valor seja positivo
        if valor <= 0:
            print("Valor de débito deve ser positivo!")
            return False

        if conta.saldo < valor:
            print("Saldo insuficiente!")
            return False

        # Garantindo que o saldo da conta n seja menor que -1000
        if not isinstance(conta, ContaPoupanca) and (conta.saldo - valor) < -1000:
            print("Erro: Contas que não são poupança não podem ter saldo abaixo de -1000.")
            return False

        conta.saldo -= valor
        print(f"Débito de R${valor:.2f} realizado na conta {numero}.")
        return True

    def transferencia(self, numero_origem, numero_destino, valor):
        conta_origem = self.contas.get(numero_origem)
        conta_destino = self.contas.get(numero_destino)

        if not conta_origem or not conta_destino:
            print("Uma ou ambas as contas não foram encontradas!")
            return False
   
        # Garatindo que o valor seja positivo
        if valor <= 0:
            print("Valor de transferência deve ser positivo!")
            return False
   
        # Garantindo que o saldo da conta n seja menor que -1000
        if not isinstance(Conta, ContaPoupanca) and (numero_origem.saldo - valor) < -1000:
            print("Erro: Contas que não são poupança não podem ter saldo abaixo de -1000.")
        
        return False

        if conta_origem.saldo < valor:
            print("Saldo insuficiente para transferência!")
            return False

        conta_origem.saldo -= valor
        conta_destino.saldo += valor
        if isinstance(conta_destino, ContaBonus):
            conta_destino.adicionar_pontos_transferencia(valor)

        print(f"Transferência de R${valor:.2f} da conta {numero_origem} para a conta {numero_destino} realizada com sucesso.")
        return True

    def render_juros(self, numero, taxa):
        conta = self.contas.get(numero)
        if not conta:
            print("Conta não encontrada!")
            return False
        if not isinstance(conta, ContaPoupanca):
            print("Apenas contas poupança podem render juros!")
            return False
        conta.render_juros(taxa)
        print(f"Juros de {taxa:.2f}% aplicados na conta {numero}.")
        return True
