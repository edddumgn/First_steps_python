def sortear(quant):
	import random
	lista = list() 
	for n in range(1,6):
		num = random.randint(1,10)
		quant.append(num)
	print(quant)
	


def somar(lst):
	soma = 0
	for n in lst:
		if n % 2 == 0:
			soma += n
	print(soma)


numeros = list()
sortear(numeros)
somar(numeros)
