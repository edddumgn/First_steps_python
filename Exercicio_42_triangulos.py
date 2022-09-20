lado1 = float(input('Digite o primeiro lado do triangulo: '))
lado2 = float(input('Digite o segundo lado do triangulo: '))
lado3 = float(input('Digite o terceiro lado do triangulo: '))

if (lado1+lado2)>lado3 and (lado1+lado3)>lado2 and (lado2+lado3)>lado1:
	print('As retas {}, {} e {} formam um triangulo!'.format(lado1, lado2, lado3))
	if lado1 == lado2 == lado3:
		print('Triangulo Equilátero')
	elif lado1==lado2!=lado3 or lado1==lado3!=lado2 or lado2==lado3!=lado1:
		print('Esse é um triangulo Isóceles!')
	elif lado1!=lado2!=lado3:
		print('Triangulo escaleno')
else:
	print('A partir dessas retas não é possivel formar um triangulo')
	
