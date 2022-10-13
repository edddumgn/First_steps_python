lista = []
while True:
	valor = int(input('Digite um valor: '))
	if valor not in lista:
		lista.append(valor)
		print('Valor adicionado com sucesso...')
	elif valor in lista:
		print('Valor duplicado! Não adicionado a lista!')
	escolha = str(input('Quer continuar[S/N]? ')).lower()
	if escolha in 'Nn':
		break
lista.sort()
print(f'Você digitou os valores {lista}')
