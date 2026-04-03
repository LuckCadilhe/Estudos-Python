def ler_matriz(nome):
    print(f"\n--- Lendo Matriz {nome} ---")
    linha = int(input("DIGITE A QUANTIDADE DE LINHAS NA MATRIZ: "))
    coluna = int(input("DIGITE A QUANTIDADE DE COLUNAS NA MATRIZ: "))

    matriz = [0] * linha

    for l in range (len(matriz)):
        matriz[l] = [0] * coluna

    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            matriz[l][c] = l * c
    print(matriz)
    return matriz

matriz1 = ler_matriz("A")
matriz2 = ler_matriz("B")

linhas = len(matriz1)
colunas = len(matriz1[0])

matriz3 = [
    [max(matriz1[l][c], matriz2[l][c]) for c in range(colunas)]
    for l in range(linhas)
    ]
print("\n Valor Maior da Matriz:")
for linha in matriz3:
    print(linha)