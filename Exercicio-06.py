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
    if item in lista:
        pedidos[item] = lista[item]
        print("Item Adicionado ao Carrinho de Compras")
    else:
        print("Item Não Encontrado no Menu!")
    

def Remover_Item():
    print("Para remover um item do carrinho digite o nome do item, para remover todos, digite 'Todos'")
    item = str(input())
    if item in pedidos:
        del pedidos[item]
        print("Item Removido do Carrinho de Compras")
    elif item == 'Todos':
        pedidos.clear()
        print("Todos os Itens Removidos do Carrinho de Compras")
    else:
        print("Item Não Encontrado no Carrinho de Compras!")

def Exibir_Pedido():
    print("Carrinho de Compras")
    print(pedidos)

def Calcular_Total():
    total = 0
    for item in pedidos:
        total += float(pedidos[item])
    print("Total: R$", total)
    print('Você Deseja Pagar?')
    print('[1] Sim \n[2] Não')
    escolha = int(input())
    if escolha == 1:
        print("Obrigado por comprar conosco!")
    elif escolha == 2:
        print("Retornando ao Menu...")
    else:
        print("Opção inválida. Por favor, escolha um número válido.")

escolha = 0
while escolha != 7:
    print("Bem-vindo ao McDonald's!")
    print('[1] Menu \n[2] Adicionar Item \n[3] Remover Item \n[4] Vizualizar Carrinho de Compras \n[5] Calcular Total \n[6] Sair \n Escolha uma opção:')

    escolha = int(input())
    if escolha == 1:
        Exibir_Menu()
        time.sleep(1)
    elif escolha == 2:
        Adicionar_Item()
        time.sleep(1)
    elif escolha == 3:
        Remover_Item()
        time.sleep(1)
    elif escolha == 4:
        Exibir_Pedido()
        time.sleep(1)
    elif escolha == 5:
        Calcular_Total()
        time.sleep(1)
    elif escolha == 6:
        print("Saindo...")
        time.sleep(1)
        exit()
    else:
        print("Opção inválida. Por favor, escolha um número válido.")
    
