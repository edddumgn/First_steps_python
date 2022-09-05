import random
alun1 = input('Nome do aluno: ')
alun2 = input('Nome do aluno: ')
alun3 = input('Nome do aluno: ')
alun4 = input('Nome do aluno: ')

escolhido = random.choice([alun1, alun2, alun3, alun4])

print(f'Dentre os alunos {alun1}, {alun2}, {alun3}, {alun4}, o escolhido foi {escolhido}')
