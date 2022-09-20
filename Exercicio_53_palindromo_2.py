frase = str(input('Digite uma frase: ')).strip().upper()
print('Você digitou a frase {}'.format(frase))

palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''

for letra in range(len(juntar)-1,-1,-1):
	inverso += juntar[letra]
print('{}  {}'.format(juntar,inverso),end='')

if juntar == inverso:
	print('\n Essa frase forma um palindromo')
else:
	print('\nEssa frase não forma um palindromo')
