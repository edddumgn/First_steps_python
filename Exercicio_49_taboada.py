#TABOADA
lista = [1,2,3,4,5,6,7,8,9,10]
tab = int(input('Digite um numero para ver sua taboada: '))
print('A taboada do {} é: '.format(tab))

for i in range(0,10):
	print('{} X {} = {}'.format(tab,lista[i],tab*lista[i]))
	
#OU


for c in range (1,11):
	print('{} X {} = {}'.format(tab,c,tab*c))
	
