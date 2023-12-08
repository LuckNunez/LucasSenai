import pandas as pd

Mes_1 = str(input("Qual o 1º Mês? "))
Mes_2 = str(input("Qual o 2º Mês? "))

dados = {
    'Meses': ['Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Janeiro','Fevereiro','Marco','Abril','Maio','Junho'],
    'Produtos': ['Camiseta','Camiseta','Camiseta','Camiseta','Camiseta','Camiseta','Bermuda','Bermuda','Bermuda','Bermuda','Bermuda','Bermuda'],
    'Vendas': [150, 100, 500, 300, 550, 100, 20, 800, 100, 12, 16, 800]
}

#Conversão para pandas "tabela = pd.DataFrame(dados)"
df = pd.DataFrame(dados)

# Print df Mês 1
df_mês = df[df['Meses'] == Mes_1]
print(df_mês)
# Print Produto Maior Venda	do Mês 1
df_Maior = df_mês['Vendas'].idxmax()
print(df_mês['Produtos'][df_Maior])

# Print df Mês 2
df_mês1 = df[df['Meses'] == Mes_2]
print(df_mês1)
# Print Produto Maior Venda	do Mês 2
df_Maior1 = df_mês1['Vendas'].idxmax()
print(df_mês1['Produtos'][df_Maior1])

# Calculo de Vendas da Camiseta
df_vendas = df_mês[df_mês['Produtos'] == 'Camiseta']
df_vendas1 = df_mês1[df_mês1['Produtos'] == 'Camiseta']

# Aumento Percentual
Aumento_Percentual = (df_vendas['Vendas'].values - df_vendas1['Vendas'].values) / df_vendas1['Vendas'].values * 100
print("Aumento Percentual de Camiseta de", Mes_1,"Para", Mes_2,"é:" , Aumento_Percentual,"%")

# Produtos mais vendidos
produto_mais_vendido = df.groupby('Produtos')['Vendas'].sum().idxmax()
print(f"O produto mais vendido é: {produto_mais_vendido}")


