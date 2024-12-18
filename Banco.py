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