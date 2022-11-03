aluno = dict()


aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('A média de {} foi: '.format(aluno['nome'])))

if aluno['media'] >= 7:
	aluno['situação'] = 'Aprovado'
elif 5 < aluno['media'] < 7:
	aluno['situação'] = 'Recuperação'
else:
	aluno['situação'] = 'Reprovado'

print('- O nome é igual a {}'.format(aluno['nome'])) 
print('- Média é igual a {}'.format(aluno['media']))
print('- A situação é igual a {}'.format(aluno['situação']))
print(aluno)
