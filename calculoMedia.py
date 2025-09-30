import math

nota1 = float(input(' digite a primeira nota: '))
nota2 = float(input(' digite a segunda nota: '))

media = (nota1 + nota2) / 2

if (nota1<0 or nota1>10) or (nota2 <0 or nota2>10):
    print('Número invalido')
else:
    print(f'O valor total da média é: {media}')