lista = []
maior = 0
menor = 0
menor_po = 0
maior_po = 0
for i in range(0,5):
	valor = int(input('Digite um valor: '))
	lista.append(valor)
	if i == 0:
		maior = valor
		maior_po = i+1
		
	elif valor > maior:
		maior = valor
		
	if i == 0:
		menor = valor
		
	elif valor <menor:
		menor = valor
		

print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior}',end='')
for posicao, v in enumerate(lista):
	if v == maior:
		print(f',na posicão .. {posicao}',end='')
print(f'\nO menor valor digitado foi {menor}',end='')
for posicao, v in enumerate(lista):
	if v == menor:
		print(f', na posição..{posicao}',end='')

