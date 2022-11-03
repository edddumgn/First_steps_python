def aumentar(preco,taxa):
	s = preco + (apreco*(taxa/100))
	print(f'Aumentando {taxa}%, temos R${s:.1f}')
	#return s
	
def diminuir(preco,taxa):
	s = preco - (preco*(taxa/100))
	print(f'Diminuindo {taxa}%, temos R${s:.1f}')
	#return s


def dobro (preco):
	s = 2*preco
	print(f'O dobro de R${preco:.1f} é R${s:.1f}')
	#return s


def metade(preco):
	s = preco/2
	print(f'A metade de R${preco:.1f} é R${s:.1f}')
	#return s
