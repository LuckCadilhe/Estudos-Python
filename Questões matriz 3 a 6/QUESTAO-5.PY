linha = int(input("DIGITE A QUANTIDADE DE LINHAS NA MATRIZ: "))
coluna = int(input("DIGITE A QUANTIDADE DE COLUNAS NA MATRIZ: "))

matriz = [0] * linha

for l in range (len(matriz)):
    matriz[l] = [0] * coluna

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = l * c
print (matriz)
busca = int(input("Digite o valor a ser pesquisado: "))

buscar = False
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] == busca:
            print(f"O valor {busca} foi encontrado na linha {l} e coluna {c}")
            buscar = True
            break
    if buscar:
        break
if not buscar:
    print("Não encontrado")