frase = str(input('Digite uma frase: ')).upper().strip()
print(frase)
print(frase[::-1])
frase2 = frase.replace(' ','')
palin = frase[::-1]
palin2 = palin.replace(' ','')
if frase2 == palin2:
	print('A frase {} é um palindromo de {}'.format(palin2,frase2))
else:
	print('A frase {} e {} NÃO são um palindromo!'.format(frase2,palin2))
