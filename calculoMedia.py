##nota1 = float(input(' digite a primeira nota: '))
##nota2 = float(input(' digite a segunda nota: '))

##media = (nota1 + nota2) / 2

##if (nota1<0 or nota1>10) or (nota2 <0 or nota2>10):
##   print('Número invalido')
##else:
##    print(f'O valor total da média é: {media}')
##-----------------------------------------------------------##
##salario = float(input('Digite seu salario: '))
##prestacao = float(input('Digite o valor do emprestimo: '))
##porcentagem = salario * 0.20

##if prestacao > porcentagem:
##        print('Emprestimo não concedido')
##else:
##        print('Empréstimo concedido')
##-----------------------------------------------------------##
##altura = float(input('Digite sua altura: '))
##genero = input('Digite seu genero: ').upper()

##if genero == 'MASCULINO':
##    peso_ideal = (72.7 * altura) - 58
##    print(f'Sua altura é {altura:.2f}m, o seu peso ideal é {peso_ideal:.2f}')
##elif genero == 'FEMININO':
##    peso_ideal = (62.1 * altura) - 44.7
##    print(f'Sua altura é {altura:.2f}m, o seu peso ideal é {peso_ideal:.2f}')
##else:
##    print('Porfavor coloque um genero correto')
##-----------------------------------------------------------##
##numero = int(input('Digite um número maior que zero: '))

##if numero <= 0:
##    print('Número invalido')
##else:
##    soma_algarismo = 0
##    numero_str = str(numero)
##
##    for algarismo in numero_str:
##        soma_algarismo += int(algarismo)
##    print(f'A soma dos algarismos do número {numero} é: {soma_algarismo}')
##-----------------------------------------------------------##

# QUESTÃO 21

##print('Escolha uma opção: \n ' \
##'1-Soma de numeros.\n ' \
##'2-Diferença entre 2 números.\n ' \
##'3- Produto entre 2 números\n ' \
##'4-Divisão entre 2 números (O denominador não pode ser zero).\n')
#opcao = int(input('Escolha uma opção a sua escolha: '))

#if opcao == 1:
#    numero1 = int(input('Digite o primeiro número: '))
#    numero2 = int(input('Digite o segundo número: '))
#    soma = numero1+numero2
#   print(f'A soma dos números escolhidos é : {soma}')

#elif opcao == 2:
    
#    numero1 = int(input('Digite o primeiro número: '))
#    numero2 = int(input('Digite o segundo número: '))
#    diferença = numero1 - numero2
#
#   if numero1 > numero2:
#        print(f'A diferença entre os numeros é: {diferença}')
#    else:
#        print(f'erro')

#elif opcao == 3:
#    numero1 = int(input('Digite o primeiro número: '))
#    numero2 = int(input('Digite o segundo número: '))
#    produto = numero1 * numero2
#
#    print(f'O resultado do produto entre os numeros é: {produto}')
#
#elif opcao == 4:
#   numero1 = int(input('Digite o primeiro número: '))
#   numero2 = int(input('Digite o segundo número: '))
#
#    if numero2 == 0:
#        print(f'O denominador não pode ser igual a ZERO')
#    else:
#        
#        divisao = numero1 / numero2
#        print(f'A divisão entre os números é: {divisao}')
##-----------------------------------------------------------##

#QUESTÃO 35
def ano_bissexto(ano):
    return (ano % 400 == 0 )or(ano % 4 == 0 and ano % 100 != 0)

dia = int(input('Digite o dia desejado: '))
mes = int(input('Digite o mês desejado: '))
ano = int(input('Digite o ano desejado: '))

if ano <= 0 or mes < 1 or mes > 12 or dia < 1 or dia > 31: 
    print('Dia, mês ou ano errado. Digite novamente!')
else:
    dias = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if ano_bissexto(ano):
        dias [2] = 29

    if dia > dias[mes]:
        print('O dia não consta no mês ou ano.')
    else:
        print(f'A data é válida.')