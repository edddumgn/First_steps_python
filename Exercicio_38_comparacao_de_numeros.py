num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
	print('O número {} é maior.'.format(num1))
elif num2 > num1:
	print('O maior numero é {}.'.format(num2))
else:
	print('Os dois numeros são iguais')
