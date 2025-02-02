class Conta:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0

    def __str__(self):
        return f"Número: {self.numero} | Saldo: R${self.saldo:.2f}"


class ContaBonus(Conta):
    def __init__(self, numero):
        super().__init__(numero)
        self.pontuacao = 10

    def adicionar_pontos_deposito(self, valor):
        self.pontuacao += int(valor // 100)

    def adicionar_pontos_transferencia(self, valor):
        self.pontuacao += int(valor // 150)

    def __str__(self):
        return super().__str__() + f" | Pontuação: {self.pontuacao}"


class ContaPoupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero)

    def render_juros(self, taxa):
        self.saldo += self.saldo * (taxa / 100)

    def __str__(self):
        return super().__str__() + " | Tipo: Conta Poupança"
