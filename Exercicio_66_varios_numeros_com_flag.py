c = 0
soma = 0
while True:
	n = int(input('Digite um numero[999 para parar]: '))
	if n == 999:
		break
	c += 1
	soma += n
print(f'Foram digitados {c} numeros, e a soma deles foi {soma}.')
