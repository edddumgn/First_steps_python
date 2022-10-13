lista_valores = [[],[]]
valor = 0
for i in range(1,8):

	valor = int(input(f'Digite o {i}* valor: '))
	if valor % 2 == 0:
		lista_valores[0].append(valor)
	elif valor % 2 == 1:
		lista_valores[1].append(valor)
print(lista_valores)

#lista_valores[0].sort()
#lista_valores[1].sort()

print(f'os valores pares digitados foram: {sorted(lista_valores[0])}')
print(f'Os valores impares digitados fora: {sorted(lista_valores[1])}')
