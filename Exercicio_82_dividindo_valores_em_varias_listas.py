lista = []
lista_par = []
lista_impar = []
while True:
	valor = int(input('Digite um valor: '))
	lista.append(valor)
	continuar = str(input('Quer continuar?[S/N] '))
	if valor % 2 == 0:
		lista_par.append(valor)
	if valor % 2 == 1:
		lista_impar.append(valor)
	if continuar in 'Nn':
		break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de impares é {lista_impar}')
