import random

def gerando_cartelas():
    numero = random.sample(range(100), 25)

    cartela = []
    for i in range(0,25,5):
        linha = numero[i:i+5]
        cartela.append(linha)
    return cartela

def exibir(cartela):
    for linha in cartela:
        print(linha)


cartela = gerando_cartelas()
exibir(cartela)