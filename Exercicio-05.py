usuarios = {
    'Admin': 'root',
    'Suporte': 'suporte',
    'Aluno': 'user'
}

usuario = input("Escreva seu Usuário: ")
senha = input("Escreva sua Senha: ")

if usuario in usuarios and senha in usuarios[usuario]:
    print("Login Bem Sucedido!")
else:
    print("Usuário ou Senha Incorreta Tente Novamente!")
  