total = 0
produto1000 = 0
c = 0
print('-'*30)
print('{:^30}'.format(' LOJA SUPER BARATÃO '))
print('-'*30)
while True:
	nome = str(input('Nome do produto: ')).lower().strip()
	preco = float(input('Preço do produto: RS'))
	c += 1
	total += preco
	if c == 1:
		preco_barato = preco
		nome_barato = nome
	if preco < preco_barato:
			preco_barato = preco
			nome_barato = nome
	if preco >= 1000:
		produto1000 += 1
	continuar = str(input('Quer continuar?[S/N] ')).lower().strip()
	if continuar not in 'NnSs':
		continuar = str(input('Quer continuar?[S/N] ')).lower().strip()
	elif continuar in 'Nn':
		break
print(f'O total gasto na compra foi de RS{total}!')
print(f'{produto1000} produtos custaram mais de RS1000,00')
print(f'O nome do produto mais barato é {nome_barato}')

		
