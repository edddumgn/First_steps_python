from random import randint
p = 'par'
i = 'impar'
c = 0
while True:
	comp = randint(1,10)
	comp_jog = 0
	n = int(input('Diga um valor: '))
	jog = str(input('Par ou impar?[P/I]: ')).strip().upper()[0]
	if jog == 'P':
		jog = p
		comp_jog = i
		if (n + comp) % 2 == 0:
			print(f'Você ganhou! você escolheu {jog} e o computador escolheu {comp_jog}, a soma foi {comp+n} {p.upper()}')
			print('Vamos jogar novamente...')
			c += 1
		else:
			if (n + comp) % 2 == 1:
				print(f'Você perdeu, você escolheu {jog} e o computador escolheu {comp_jog}, a soma foi {comp+n} {i.upper()}')
				break
	if jog == 'I':
		jog = i
		comp_jog = p
		if (n + comp) % 2 == 1:
			print(f'Você ganhou! você escolheu {jog} e o computador escolheu {comp_jog}, a soma foi {comp+n} {i.upper()}')
			print('Vamos jogar novamente...')
			c += 1
		else:
			if (n + comp) % 2 == 0:
				print(f'Você perdeu, você escolheu {jog} e o computador escolheu {comp_jog}, a soma foi {comp+n} {i.upper()}')
				break
print(f'GAME OVER! Você ganhou {c} vezes!')
