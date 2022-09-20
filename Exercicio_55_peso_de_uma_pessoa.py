peso_menor = 100000
peso_maior = 0
for pessoa in range(1,6):
	peso = float(input('O peso da {}* pessoa é: '.format(pessoa)))
	if peso_maior <= peso:
		peso_maior = peso
	elif peso_menor >= peso:
		peso_menor = peso
print('O maior peso lido foi {:.1f}KG!'.format(peso_maior))
print('O menor peso lido foi {:.1f}KG!'.format(peso_menor))
	
