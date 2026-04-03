def consultar_distancia():
    matriz_distancia = [
        [0,  15, 30, 5,  12],  # Cidade 0
        [15, 0,  10, 17, 28],  # Cidade 1
        [30, 10, 0,  3,  11],  # Cidade 2
        [5,  17, 3,  0,  80],  # Cidade 3
        [12, 28, 11, 80, 0]   # Cidade 4
    ]
    distancia_total = 0
    percurso = []

    print("Cidade que estão proximas: 0, 1, 2, 3, 4")
    for i in range(1,7):
        print(f"\nCoordenada {i}/6: ")
        try:
            origem = int(input("\nEscolha a cidade de ORIGEM (0-4): "))
            destino = int(input("Escolha a cidade de DESTINO (0-4): "))
            if 0 <= origem < 5 and 0 <= destino < 5:
                distancia = matriz_distancia[origem][destino]
                distancia_total += distancia
                percurso.append(str(distancia))

                print(f"  Distância do trecho ({origem},{destino}): {distancia} km")
            else:
                print("\nErro: Cidade errada. Digite os numeros corretos de 0 a 4")
            
            if i < 6:
                continuar = input("\nDeseja adicionar mais um trecho? (s/n): ").lower()
                if continuar != 's':
                    break
            else:
                print("\nLimite total de 6 trechos atingido")
                
        except ValueError:
            print("\nErro: Digite apenas números inteiros")
    if percurso:
        soma = " + ".join(percurso)
        print(f"Calculo da distancia: {soma}")
        print(f"Total percorrido: {distancia_total} km")
    else:
        print("\nNão houve percurso registrado")

consultar_distancia()