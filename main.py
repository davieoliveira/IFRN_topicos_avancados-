from Banco import Banco

def executar_banco():
    banco = Banco()
    while True:
        print("\n=== Menu do Banco ===")
        print("1. Cadastrar Conta")
        print("2. Consultar Saldo")
        print("3. Crédito")
        print("4. Débito")
        print("5. Transferência")
        print("6. Ver Contas")
        print("7. Render Juros (Conta Poupança)")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                numero = int(input("Informe o número da conta: "))
                tipo = input("Tipo da conta (simples/bonus/poupanca): ").lower()
                banco.cadastrar_conta(numero, tipo)
            except ValueError:
                print("Dados inválidos!")

        elif opcao == "2":
            try:
                numero = int(input("Informe o número da conta: "))
                banco.consultar_saldo(numero)
            except ValueError:
                print("Número da conta inválido!")

        elif opcao == "3":
            try:
                numero = int(input("Informe o número da conta: "))
                valor = float(input("Informe o valor do crédito: "))
                banco.credito(numero, valor)
            except ValueError:
                print("Valores inválidos!")

        elif opcao == "4":
            try:
                numero = int(input("Informe o número da conta: "))
                valor = float(input("Informe o valor do débito: "))
                banco.debito(numero, valor)
            except ValueError:
                print("Valores inválidos!")

        elif opcao == "5":
            try:
                numero_origem = int(input("Informe o número da conta de origem: "))
                numero_destino = int(input("Informe o número da conta de destino: "))
                valor = float(input("Informe o valor da transferência: "))
                banco.transferencia(numero_origem, numero_destino, valor)
            except ValueError:
                print("Valores inválidos!")

        elif opcao == "6":
            banco.ver_contas()

        elif opcao == "7":
            try:
                numero = int(input("Informe o número da conta: "))
                taxa = float(input("Informe a taxa de juros (%): "))
                banco.render_juros(numero, taxa)
            except ValueError:
                print("Valores inválidos!")

        elif opcao == "8":
            print("Saindo do sistema bancário.")
            break

        else:
            print("Opção inválida. Tente novamente.")

executar_banco()
