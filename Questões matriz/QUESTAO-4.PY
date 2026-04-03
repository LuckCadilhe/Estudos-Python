linha = int(input("DIGITE A QUANTIDADE DE LINHAS NA MATRIZ: "))
coluna = int(input("DIGITE A QUANTIDADE DE COLUNAS NA MATRIZ: "))

matriz = [0] * linha
for l in range (len(matriz)):
    matriz[l] = [0] * coluna
maior_valor = [0][0]
lin_max = 0
col_max = 0

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = l * c
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] >= maior_valor:
            maior_valor = matriz[l][c]
            lin_max = l
            col_max = c

print(f"Maior valor: {maior_valor}")
print(f"Localização : Linha {lin_max} Coluna {col_max}")