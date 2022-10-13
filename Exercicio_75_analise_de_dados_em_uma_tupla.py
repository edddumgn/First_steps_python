n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
n4 = int(input('Digite um numero: '))
c9 = 0
cpar = 0
valores = (n1,n2,n3,n4)
print(f'Você digitou os valores {valores}')
for n in valores:
	if n == 9:
		c9 += 1
	if n % 2 == 0:
		cpar += 1
print(f'O valor 9 apareceu {c9} vezes')
if 3 in valores:
	print(f'O primeiro valor 3 está na posição {valores.index(3)+1}')
else:
	print('O valor 3 não foi encontrado')
print(f'Foram digitados {cpar} numeros pares')


