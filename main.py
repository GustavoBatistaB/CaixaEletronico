
def verificarConta(nome, senha, valorConta, acesso):

    loopConta, loop_1 = True, 0
    while loopConta:
        print("-------------------------------------")
        print("           Senha")
        print("-------------------------------------")
        digiteSenha = input("Digite a Sua Senha Numerica ")
        if digiteSenha == senha:
            print("Seja Bem Vindo (a)", nome)
            print("Saldo na Conta: ", valorConta)
            loopConta, acesso = False, True
        else:
            loop_1 += 1
            print("Senha Errada")
            if loop_1 > 3:
                print("Senha Bloqueada")
                loopConta, acesso = False, False

    print("-------------------------------------")
    return valorConta, acesso

###############################################################################


def depositarDinheiro(valorConta, saldoCaixa):
    print("-------------------------------------")
    print("            Depositar")
    print("-------------------------------------")
    valorDeposito = int(input("Quanto Deseja Depositar ? "))
    saldoCaixa += valorDeposito
    valorConta += valorDeposito
    print(f"Parabens Seu novo saldo é:  {valorConta}")
    print("-------------------------------------")
    return valorConta, saldoCaixa

###############################################################################


def sacarDinheiro(valorConta, saldoCaixa):
    print("-------------------------------------")
    print("       Sacar Dinheiro")
    print("-------------------------------------")
    valor = float(input("Digite um valor para sacar "))
    if valor <= saldoCaixa and valor <= valorConta:
        saldoCaixa -= valor
        valorConta -= valor
        print(f"Valor do saque : {valor}")
        print(f"Seu novo saldo é de: {valorConta}")

    else:
        if valor > saldoCaixa:
            print("Caixa não tem dinheiro")
            print(saldoCaixa)

        else:
            print(f"Saldo insuficiente \nSaldo atual {valorConta}")
    return valorConta, saldoCaixa

###############################################################################


saldoCaixa = 100

dadosClientes = {"SUL33": ("Suellen", "000", 2000), "VIC17": ("Vitoria", "001", 2000),   "NES26": ("Vanessa", "002", 1500), "FRN18": ("Francisca", "003", 2500)}
#idCliente = "vic17"

print("-------------------------------------")
print("         Caixa Eletronico")
print("-------------------------------------")

acesso = not(False)
loopInicio = True

global nome, senha, valorConta


while loopInicio:
    idCliente = input("Digite o ID da conta ")
    idCliente = idCliente.upper()
    if not(idCliente in dadosClientes) and idCliente != "2070":
        print("-------------------------------------")
        print("Não Existe um Cliente com Esse ID ")
        print("-------------------------------------")
    elif idCliente == "2070":
        print("-------------------------------------")
        print("          Em Manutenção ")
        print("-------------------------------------")
        loopInicio = False

    else:
        nome, senha, valorConta = list(dadosClientes[idCliente])
        valorConta, acesso = verificarConta(nome, senha, valorConta, acesso)
        if acesso:
            loopEncerar = True
            while loopEncerar:
                opcao = input("Escolha uma Opção \n1 - Depositar Dinheiro  \n2 - Sacar Dinheiro \nS - Sair \n")
                opcao = opcao.lower()
                if opcao == "1":
                    valorConta, saldoCaixa = depositarDinheiro(valorConta, saldoCaixa)
                elif opcao == "2":
                    valorConta, saldoCaixa = sacarDinheiro(valorConta, saldoCaixa)
                elif opcao == "s":
                    print("Saindo da Conta")
                    loopEncerar = False
                else:
                    print("Opcão Invalida")

            dadosClientes[idCliente] = (nome, senha, valorConta)
