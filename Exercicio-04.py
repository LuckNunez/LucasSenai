Distancia = float(input("Informe a Distância Percorrida em KM: "))
Tipo_veiculo = str(input("Informe o Veiculo do Usuário (Ex: Carro, Moto e Bicicleta): "))

if Tipo_veiculo == "Carro":
    Custo_por_Km = 0.50
elif Tipo_veiculo == "Moto":
    Custo_por_Km = 0.20
elif Tipo_veiculo == "Bicicleta":
    Custo_por_Km = 0.10
else:
    print("Tipo de Véiculo Inválido")
    exit()

Calcular_Custo_Total = Distancia*Custo_por_Km
print("Custo total da viagem: R$ ",Calcular_Custo_Total)


