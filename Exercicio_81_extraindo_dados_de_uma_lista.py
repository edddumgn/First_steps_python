cont = 0
lista = []
while True:
	valor = int(input('Digite um valor: '))
	lista.append(valor)
	cont += 1
	continuar = str(input('Quer continuar?[S/N] '))
	if continuar in 'Nn':
		break
print('-='*30)
print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
	print('O valor 5 faz parte da lista')
else: 
	print('Na lista não há o valor 5')

