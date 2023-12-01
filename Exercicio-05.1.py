usuarios = {
    'Admin': 'root'
}

def cadastrar_usuario():
    print("Vamos cadastrar seu usuário!")
    novo_usuario = input("Digite o nome do Usuário: ")
    if novo_usuario in usuarios:
        print("Usuário já tem Cadastro")
    else:
        usuario = input("Digite Sua Senha: ")
        usuarios[novo_usuario] = usuario
        print("Usuário Cadastrado")
    print(usuarios)
    

def Fazer_Login():
    print("Vamos Fazer Login no Sistema!")
    usuario = input("Digite Seu Usuário: ")
    senha = input("Digite sua Senha: ")
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login Bem Sucedido!")
    else:
        print("Usuário ou Senha Incorreta Tente Novamente!")


escolha = 0
while escolha != 3:
    print('[1] Cadastrar Usuário \n[2] Fazer Login \n[3] Encerrar Programa')
    escolha = int(input("Escolha uma das Opções: "))
    if escolha == 1:
        cadastrar_usuario()
    elif escolha == 2:
        Fazer_Login()
    else:
        print("Programa Encerrado")
    
        
        

