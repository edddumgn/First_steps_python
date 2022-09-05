import random
alun1 = input('Nome do aluno: ')
alun2 = input('Nome do aluno: ')
alun3 = input('Nome do aluno: ')
alun4 = input('Nome do aluno: ')

alunos = [alun1, alun2, alun3, alun4]
random.shuffle(alunos)
print(f'A ordem sorteada foi {alunos}')
