x = (
'Lápis',1.75,'Borracha',2.0,'Caderno',15.90,'Estojo',25,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90
)

print('-'*40)
print('{:^40}'.format(' TABELA DE PREÇOS '))
print('-'*40)
for item in range(0,len(x)):
	if item %2 ==0:
		print(f'{x[item]:.<30}',end='')
	else:
		print(f'R${x[item]:>8.2f}')
