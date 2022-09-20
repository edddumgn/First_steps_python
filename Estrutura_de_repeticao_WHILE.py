n = 1
while n != 0:
	n = int(input('Digite um numero: '))
print('FIM')





num = 1
par = impar = 0
while num != 0:
	num = int(input('Digite um numero: '))
	if num %2 == 0:
		par += 1
	else:
		impar += 1
print('Foram digitados {} numeros pares e {} numeros impares!'.format(par, impar))
	
	 
