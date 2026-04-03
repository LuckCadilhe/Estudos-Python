def matriz():
    linha = int(input("DIGITE A QUANTIDADE DE LINHAS NA MATRIZ: "))
    coluna = int(input("DIGITE A QUANTIDADE DE COLUNAS NA MATRIZ: "))

    matriz = [0] * linha
    for l in range (len(matriz)):
        matriz[l] = [0] * coluna
    return matriz, linha, coluna

matriz, linhas, colunas = matriz()
soma_impares = 0

for l in range(linhas):
    for c in range(colunas):
        valor = int(input(f"Digite o valor para {l} e {c}: "))
        matriz[l][c] = valor

        if valor % 2 != 0:
            soma_impares += valor
print("\nValor Matriz")
for l in matriz:
    print(l)

for c in range(colunas):
    soma_coluna = 0
    for l in range(linhas):
        soma_coluna += matriz[l][c]
    print(f"A soma das colunas {c}: {soma_coluna}")

for l in range(linhas):
    soma_linhas = 0
    for c in range(colunas):
        soma_linhas += matriz[l][c]
    print(f"A soma das linhas {l}: {soma_linhas}")

print(f"\nA soma do impares é: {soma_impares}")