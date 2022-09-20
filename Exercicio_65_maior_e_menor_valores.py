resp = 'S'
c = 0
soma = 0
n = 0
while resp in 'Ss':
	
	n = int(input('Digite um numero: '))
	
	c += 1
	soma += n
	if c == 1:
		maior = menor = n
	else:
		if maior < n:
			maior = n
		elif menor > n:
			menor = n
	

	resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
print('Foram digitados {} numeros, e a média entre eles é {}!'.format(c,soma/c)) 
print('O maior numero foi {}, e o menor numero foi {}!'.format(maior,menor))
print('Acabou')	
