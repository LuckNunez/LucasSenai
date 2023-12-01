idade = int(input ("digite sua idade: "))

if idade >=0 and idade <= 11:
    print ("usuário é uma criança!")

elif idade >=12 and idade <=17:
    print ("usuário é um adolescente!")

elif idade >=18  and idade <=25:
    print ("usuário é um jovem!")

elif idade >=26  and idade <=60:
    print ("usuário é um adulto!")

elif idade >=60:
    print ("usuário é um idoso!")