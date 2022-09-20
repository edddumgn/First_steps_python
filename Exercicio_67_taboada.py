t = 'TABOADA'
print(f'{t:-^20}')
while True:
	n = int(input('Digite um numero: '))
	if n < 0:
		break
	for i in range(1,11):
		print(f'{n} X {i} = {n*i}')
 
print(f'Programa {t} encerrado! Volte sempre!')
