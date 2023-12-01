import time
lista = {
    'Big Mac' : '15.90',
    'McChicken' : '12.90',
    'Cheeseburger' : '9.90',
    'McFish' : '11.90',
    'McFlurry' : '7.90'
}
pedidos = {

}

def Exibir_Menu():
    print("Bem-vindo ao McDonald's!")
    print("Menu:")
    print(lista)

def Adicionar_Item():
    print("Adicionar Item ao Pedido")
    item = str(input())
    pedidos = lista[item]
    if item in lista:
        print("Item Adicionado ao Carrinho de Compras")
    else:
        print("Item Não Encontrado no Menu!")
    

def Remover_Item():
    print("Remover Item do Carrinho de Compras")
    item = int(input())
    del pedidos[item]
    print("Item Removido do Carrinho de Compras")

def Exibir_Pedido():
    print("Carrinho de Compras")
    print(pedidos)

def Calcular_Total():
    total = 0
    for item in pedidos:
        total += float(pedidos[item])
    print("Total: R$", total)

escolha = 0
while escolha != 7:
    print("Bem-vindo ao McDonald's!")
    print('[1] Menu \n[2] Adicionar Item \n[3] Remover Item \n[4] Vizualizar Carrinho de Compras \n[5] Calcular Total \n[6] Sair \n Escolha uma opção:')

    escolha = int(input())
    if escolha == 1:
        Exibir_Menu()
        time.sleep(5)
    elif escolha == 2:
        Adicionar_Item()
        time.sleep(5)
    elif escolha == 3:
        Remover_Item()
        time.sleep(5)
    elif escolha == 4:
        Exibir_Pedido()
        time.sleep(5)
    elif escolha == 5:
        Calcular_Total()
        time.sleep(5)
    elif escolha == 6:
        print("Saindo...")
        time.sleep(5)
        exit()
    else:
        print("Opção inválida. Por favor, escolha um número válido.")
    
