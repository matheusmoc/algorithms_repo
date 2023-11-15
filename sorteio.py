import random

# alunos = ["Kauan", "Ana", "Julia", "Mila", "Sarah", "Denis", "Matheus"]
# random.shuffle(alunos)

# # Lista de questões
# questoes = list(range(1, 10))  # Gera uma lista de questões de 1 a 10
# random.shuffle(questoes)

# # Distribuir questões para os alunos
# distribuicao = {
#     aluno: [] 
#     for aluno in alunos  
# }

# # Distribuir as questões
# for aluno in alunos:
#     if questoes:
#         questao = questoes.pop()
#         distribuicao[aluno].append(questao)

# # Distribuir as questões restantes, se houver
# while questoes:
#     for aluno in alunos:
#         if questoes:
#             questao = questoes.pop()
#             distribuicao[aluno].append(questao)

# # Imprimir a distribuição
# for aluno, questoes_do_aluno in distribuicao.items():
#     print(f"{aluno} recebeu as questões {questoes_do_aluno}") melhore esse codigo usando metodos magicos


alunos = ["Kauan", "Ana", "Julia", "Mila", "Sarah", "Denis", "Matheus"]
questoes = list(range(1, 40))
random.shuffle(alunos)
random.shuffle(questoes)

distribuicao = {aluno: [] for aluno in alunos}

while questoes:
    for aluno in alunos:
        if questoes:
            questao = questoes.pop()
            distribuicao[aluno].append(questao)

for aluno, questoes_do_aluno in distribuicao.items():
    print(f"{aluno} recebeu as questões {questoes_do_aluno}")