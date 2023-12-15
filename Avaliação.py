Armazenamento_Conta = {
    '010785':'4200',
    '178549':'6500',
    '859479':'7000',
    '718547':'6750',
    '536748':'1700'
}

print("Vamos Autenticar Sua Conta, Por Favor Digite a Senha da Sua Conta.")
Senha = input("Digite sua Senha: ")
if Senha in Armazenamento_Conta:
    print("Autenticação Concluida")
else:
    print("Senha Incorreta.")

Saldo = Armazenamento_Conta[Senha]
Manipulação = float(Saldo)

def Verificar_Saldo():
    print(Saldo)

def Depositar_Saldo():
    print("Quanto Você Deseja Depositar?")
    depositar = float(input())
    Manipular = Manipulação+depositar
    Saldo = Armazenamento_Conta[Manipular]
    print(Saldo)

def Retirar_Saldo():
    print("Quanto Você Deseja Retirar?")
    retirar = float(input())
    Manipular = Manipulação-retirar
    Saldo = Armazenamento_Conta[Manipular]
    print(Saldo)

def Sair():
    print("Programa encerrado!")

escolha = 0
while escolha != 4:
    print('[1] Verificar Saldo \n[2] Depositar Saldo \n[3] Retirar Saldo \n[4] Encerrar Programa')
    escolha = int(input("Bem Vindo ao Seu Menu Interativo, Escolha uma das Opções: "))
    if escolha == 1:
        Verificar_Saldo()
    elif escolha == 2:
        Depositar_Saldo()
    elif escolha == 3:
        Retirar_Saldo()
    else:
        Sair()




