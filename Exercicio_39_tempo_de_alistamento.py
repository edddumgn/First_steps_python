from datetime import date
nascimento = int(input('Digite o ano em que você nasceu: '))
date = date.today().year

if date - nascimento < 18:
	atraso = 18 - (date - nascimento)
	print('você precisa se alistar! Faltam {} anos!'.format(atraso))
elif date - nascimento > 18:
	tempo = (date - nascimento)- 18
	print('Você esta atrasado com o alistamento em {} anos!'.format(tempo))
else:
	print('Esta na hora de você se alistar')
