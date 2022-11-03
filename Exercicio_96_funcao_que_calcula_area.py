def area(l,c):
	s = l * c
	print(f'A área desse terreno {l}X{c} é de {s}m2.')
	
	
print('  Controle de Terrenos ')
print('-'*25)
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(c): '))
area(l,c)

