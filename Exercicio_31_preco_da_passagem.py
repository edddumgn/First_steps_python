dist = int(input('Qual a distancia de viagem? '))
if dist <= 200:
	preco = dist*0.50
	print('O preço da passagem é de {}!'.format(preco))
else:
	preco = dist*0.45
	print('O preço da passagem é de {}!'.format(preco))
