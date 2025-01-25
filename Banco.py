from Conta import Conta

class Banco:
    def __init__(self):
        self.contas = {}  

    def cadastrar_conta(self, numero):
        if numero in self.contas:
            print("Conta já existe!")
            return False

        self.contas[numero] = Conta(numero)
        
        print(f"Conta {numero} cadastrada com sucesso.")
        return True
    
    def ver_contas(self):
        
        if not self.contas:
            print("Nenhuma conta cadastrada.")
        for conta in self.contas.values():
            print(conta)

        return True

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
        if valor <= 0:
            print("Valor de crédito deve ser positivo!")
            return False
        
        conta.saldo += valor
        
        print(f"Crédito de R${valor:.2f} realizado na conta {numero}.")
        return True

    def debito(self, numero, valor):
        conta = self.contas.get(numero)
        
        if not conta:
            print("Conta não encontrada!")
            return False

        # Garantindo que o valor seja positivo.    
        if valor <= 0:
            print("Valor de débito deve ser positivo!")
            return False
            
        if conta.saldo < valor:
            print("Saldo insuficiente!")
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
        if valor <= 0:
            print("Valor de transferência deve ser positivo!")
            return False
        if conta_origem.saldo < valor:
            print("Saldo insuficiente para transferência!")
       
            return False
       
        conta_origem.saldo -= valor
        conta_destino.saldo += valor
        print(f"Transferência de R${valor:.2f} da conta {numero_origem} para a conta {numero_destino} realizada com sucesso.")
        return True