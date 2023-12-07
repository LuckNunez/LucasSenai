# Importação com library Pandas
# Realizando importações com bibliotecas utilizando o recurso "VENV"

import pandas as pd

dados = {
    'Nome': ['Lucas','Samuel','Davi','Jadson'],
    'Idade': [22,19,18,21],
    'Cidade': ['Camaçari','São Paulo','Salvador','Rio de Janeiro'],
}

#Conversão para pandas "tabela = pd.DataFrame(dados)"
df = pd.DataFrame(dados)
#print (tabela)

for dado in df.values:
    #print(dado)
    print(dado[0],dado[1],dado[2])
