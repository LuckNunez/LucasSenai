Usuarios = {
    'Usuario1' : 'Senha1',
    'Usuario2' : 'Senha2'
}

Login = str(input("Qual o seu login?"))
Senha = str(input("Qual a sua senha?"))

if Login in Usuarios and Senha in Usuarios[Login]:
    print('Login Bem Sucedido')
else:
    print('Usuario ou senha incorreta.')