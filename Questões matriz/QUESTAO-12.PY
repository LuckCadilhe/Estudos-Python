def correcao_provas():
    gabarito = []
    for l in range (1,11):
        resposta = input(f"Digite a resposta {l} (a, b, c, d ou e): ")
        gabarito.append(resposta)
    
    resultado = []

    for aluno in range(1,4):
        print(f"Dados aluno {aluno}")
        matricula = int(input("Digite a matricula: "))
        resposta_aluno=[]
        nota = 0
    
    for questao in range(1,11):
        resp_aluno = input(f"Resposta da questão {questao}: ")
        resposta_aluno.append(resp_aluno)

        if resp_aluno == gabarito[questao - 1]:
            nota +=1
    resultado.append({"matricula": matricula, "nota": nota})

    for res in resultado:
        print(f"Matricula: {res['matricula']} | Nota Final: {res['nota']} / 10")
correcao_provas()