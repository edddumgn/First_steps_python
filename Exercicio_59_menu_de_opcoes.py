from time import sleep
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

n = 0 
fim ='FINALIZANDO ... ' 

while n != 5:
	print('''
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
''')
	n = int(input('>>>> Qual é a sua opção? '))
	if n == 1:
		print('A soma entre {} + {} é {}!'.format(num1,num2,num1+num2))
		print('-='*20)
	if n == 2:
		print('A multiplicação {} X {} é {}!'.format(num1,num2,num1*num2))
		print('-='*20)
	if n == 3:
		if num1 > num2:
			print('Entre {} e {} o maior valor é {}.'.format(num1,num2,num1))
			print('-='*20)
		elif num1 < num2:
			print('Entre {} e {} o maior valor é {}.'.format(num1,num2,num2))
			print('-='*20)
		else:
			print('Os dois numeros são iguais!')
			print('-='*20)
	elif n == 4:
		num1 = int(input('Digite o primeiro numero: '))
		num2 = int(input('Digite o segundo numero: '))
		print('-='*20)
	elif n > 5 or n < 1:
		print('Opção invalida! Tente novamente!')

for i in fim:
	sleep(0.2)
	print(i,end='',flush=True)
	
