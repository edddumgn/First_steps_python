x = ('mesa', 'ventilador', 'cama', 'porteira', 'barraca', 'abajur', 'panela', 'ponteiro', 'fotografia')

for palavra in x:
	print(f'\nNa palavra {palavra.upper()} temos',end=' ')
	for letra in palavra:
		if letra in 'aeiou':
			print(letra,end=' ')
