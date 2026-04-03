linha = int(input("DIGITE A QUANTIDADE DE LINHAS NA MATRIZ: "))
coluna = int(input("DIGITE A QUANTIDADE DE COLUNAS NA MATRIZ: "))

matriz = [0] * linha
for l in range (len(matriz)):
    matriz[l] = [0] * coluna
tam = linha*coluna

for l in range(len(matriz[l])):
    matriz[l][l] = 1
for linha in matriz:
    print(linha)