import random
print('-'*40)
print('{:^40}'.format(' JOGAR NA MEGA SENA '))
print('-'*40)

sortear = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=-=-= SORTEANDO {:^5} JOGOS -=-=-='.format(sortear))

for i in range(1,sortear+1):
	numeros = random.sample(range(1,100),6)
	print(f'Jogo {i}: {numeros}')

print('\n-=-=-=-=-=-=< BOA SORTE! >-=-=-=-=-=-=')
