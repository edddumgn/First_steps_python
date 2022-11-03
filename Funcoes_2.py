def somar(a=0,b=0,c=0): #Parametros opcionais
	'''
	-> Faz a soma de três valores e mostra o resultado na tela. 
	:param a: o primeiro valor
	:param b: o segundo valor
	:param c: o terceiro valor
	'''
	s = a + b + c
	print(f'A soma vale {s}')

somar(3)



def teste():
	global a
	a = 8
	b = 4
	c = 2
	print(f'A dentro vale {a}')
	print(f'B dentro vale {b}')
	print(f'C dentro vale {c}')

a = 1
teste()
print(a)
