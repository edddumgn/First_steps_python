lista = []
for x in range(0,5):
	n = int(input('Digite um numero: '))
	if x == 0:
		lista.append(n)
	elif n > lista[-1]:
		lista.append(n)
	else:
		pos = 0
		while pos < len(lista):
			if n <= lista[pos]:
				lista.insert(pos, n)
				break
			pos += 1
print(f'Os valores digitados foram {lista}')
