linha = int(input("DIGITE A QUANTIDADE DE LINHAS NA MATRIZ: "))
coluna = int(input("DIGITE A QUANTIDADE DE COLUNAS NA MATRIZ: "))


matriz = [0] * linha
for l in range (len(matriz)):
    matriz[l] = [0] * coluna

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = l * c
print(matriz)