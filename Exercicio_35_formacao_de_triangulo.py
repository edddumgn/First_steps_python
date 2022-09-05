reta1 = float(input('Tamanho da primeira reta: '))
reta2 = float(input('Tamanho da segunda reta: '))
reta3 = float(input('Tamanho da terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
	print('É possivel formar um triangulo')
else:
	print('Não é possivel a formação de um triangulo')
