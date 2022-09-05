num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))

maior = num1
if num2>num1 and num2>num3:
	maior = num2
if num3>num1 and num3>num2:
	maior = num3

menor = num1
if num2<num1 and num2<num3:
	menor = num2
if num3<num1 and num3<num2:
	menor = num3



print('O maior numero é o {}!'.format(maior))
print('O menor numero é o {}!'.format(menor))
	
