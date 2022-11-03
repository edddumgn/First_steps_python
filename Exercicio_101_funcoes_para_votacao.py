
n = int(input('Em que ano você nasceu? '))

def votar(ano):
	from datetime import date
	x = date.today().year
	z = x - ano
	if z < 16:
		print(f'Com {z} anos: NÃO é permitido votar')
	elif z > 17:
		print(f'Com {z} anos: O voto é OBRIGATÓRIO')
	else:
		print(f'Com {z} anos: O voto é OPCIONAL')

votar(n)
