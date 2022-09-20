nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) // 2

if media < 5.0:
	print('Que pena! Você foi reprovado!')
elif media >= 5.0 and media <= 6.9:
	print('Você ficou de recuperação! Estude!')
else:
	print('Você tirou {} e conseguiu passar! Parabéns!'.format(media))
	 
