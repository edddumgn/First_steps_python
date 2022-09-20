soma = 0
c = 0
num = int(input('Digite um numero[999 para parar]: '))
while num != 999:
	soma = soma + num
	c += 1
	num = int(input('Digite um numero[999 para parar]: '))
print('Você digitou {} numeros!'.format(c))
print('A soma de todos os numeros foi {}!'.format(soma))

