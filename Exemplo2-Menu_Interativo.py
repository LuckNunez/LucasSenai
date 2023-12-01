from tkinter import *
janela = Tk()
janela.title("McDonald's")
texto = Label(janela, text="Escolha uma das opções:")
texto.grid(column=0, row=0, padx=10, pady=10)

def botao_menu():
    Exibir_Menu()

def botao_adicionar_item():
    Adicionar_Item()

def botao_remover_item():
    Remover_Item()

def botao_visualizar_carrinho():
    Exibir_Pedido()

def botao_calcular_total():
    Calcular_Total()

def botao_sair():
    print("Saindo...")
    janela.destroy()

botao_menu = Button(janela, text="Menu", command=botao_menu)
botao_menu.grid(column=0, row=1, padx=10, pady=20)

botao_adicionar = Button(janela, text="Adicionar Item", command=botao_adicionar_item)
botao_adicionar.grid(column=0, row=2, padx=10, pady=20)

botao_remover = Button(janela, text="Remover Item", command=botao_remover_item)
botao_remover.grid(column=0, row=3, padx=10, pady=20)

botao_visualizar = Button(janela, text="Visualizar o Carrinho", command=botao_visualizar_carrinho)
botao_visualizar.grid(column=0, row=4, padx=10, pady=20)

botao_calcular = Button(janela, text="Calcular Total", command=botao_calcular_total)
botao_calcular.grid(column=0, row=5, padx=10, pady=20)

botao_sair = Button(janela, text="Sair", command=botao_sair)
botao_sair.grid(column=0, row=6, padx=10, pady=20)

# Rótulo para exibir mensagens
texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=7, padx=10, pady=10)

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

janela.mainloop()