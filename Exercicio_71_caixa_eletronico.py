print('-'*40)
print('{:^40}'.format(' CAIXA ELETRÔNICO '))
print('-'*40)
c50 = 0
c20 = 0
c10 = 0
c1 = 0
valor = int(input('Qual será o valor sacado? R$'))
while valor != 0:
	while valor >= 50:
		valor = valor - 50
		c50 += 1
	while valor >= 20:
		valor = valor - 20
		c20 += 1
	while valor >= 10:
		valor = valor - 10
		c10 += 1
	while valor > 0:
		valor = valor - 1
		c1 += 1


print('Total de ' ,end='')
if c50 >=1:
	print(f'{c50} cédulas de R$50,00',end='')

if c20 >=1:
	print(f', {c20} cédulas de R$20,00',end='')
	
if c10 >=1:
	print(f', {c10} cédulas de R$10,00',end='')
	
if c1 >=1:
	print(f', {c1} cédulas de R$1,00',end='')
	
		
		
