def fatorial_iterativo(n):
    f=1
    for i in range(1, n+1):
        f=f*i
    return f

numero = 4

print(f'O fatorial de {numero} é: {fatorial_iterativo(numero)}')