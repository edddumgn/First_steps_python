velocidade = float(input('Velocidade do carro: '))
if velocidade > 80:
	print('Você foi mutado!')
	multa = (velocidade - 80)*7
	print('Preço da multa de R${:.2f}!'.format(multa))
print('Boa viagem')
