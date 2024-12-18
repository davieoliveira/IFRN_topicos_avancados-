class Conta:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0

    def __str__(self):
        return f"Número: {self.numero} | Saldo: R${self.saldo:.2f}"
