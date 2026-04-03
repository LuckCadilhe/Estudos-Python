linha = int(input("DIGITE A QUANTIDADE DE LINHAS NA MATRIZ: "))
coluna = int(input("DIGITE A QUANTIDADE DE COLUNAS NA MATRIZ: "))
matriz = [0] * linha
for l in range (len(matriz)):
    matriz[l] = [0] * coluna
tam = linha*coluna
valores = [int] * tam
cont = 0

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input("Digite o valor: "))
        if matriz[l][c] > 10:
            valores[cont] = matriz[l][c]
            cont = cont +1

for l in range(len(matriz)):
    print (matriz[l])

print(valores)
print(cont)