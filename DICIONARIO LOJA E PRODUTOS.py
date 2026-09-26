import os
lista = []
for i in range(3):
    produto = {
        "nome": input("Digite o nome do produto: "),
        "preco": float(input("Digite o preço do produto: ")),
        "quantidade": int(input("Digite a quantidade do produto: "))
    }
    input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear') #Limpa a tela do terminal
    lista.append(produto)
for i in lista:
    print(f"Lista de produtos: nome: {i['nome']}, preço R$: {i['preco']}, quantidade: {i['quantidade']}")  