gabarito= ['a','b','c','d','c','d','b','a','a','d']

respostas = []
print("Digite as repostas dos alunos (a, b, c, d): ")

for c in range(5):
    alunos = []
    print(f"Aluno {c+1}")
    for l in range(10):
        resposta_aluno = input(f"Questão {l+1}: ").lower().strip()
        alunos.append(resposta_aluno)
    respostas.append(alunos)

resultado= [0] * 5

for c in range(5):
    pontos = 0
    for l in range(10):
        if respostas[c][l] == gabarito[l]:
            pontos += 1
    resultado[c] = pontos

print(" Pontuação dos Alunos: ")
for i in range(5):
    print(f"Aluno {c+1}: {resultado[c]}")