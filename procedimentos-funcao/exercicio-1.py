def ehPar(n):
    r = (n%2==0)
    return r

def soma_par(lsta):
    soma = 0
    for num in lsta:
        if(ehPar(num)):
            soma=soma+num
    return soma

lista = [10, 2, 5, 14, 6, 4]
soma = soma_par(lista)
print(f'O somatório dos elementos pares da lista é: {soma}')