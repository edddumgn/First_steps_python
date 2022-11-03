import random
from operator import itemgetter
jogadores = dict()

print('Valores Sorteados:')

jogadores['jogador1'] = random.randint(1,6)
jogadores['jogador2'] = random.randint(1,6)
jogadores['jogador3'] = random.randint(1,6)
jogadores['jogador4'] = random.randint(1,6)

print(jogadores)

for k, v in jogadores.items():
	print('O {} tirou {} no dado.'.format(k,v))
	
print('-='*35)
print('=={}=='.format(' RANKING DOS JOGADORES '))

ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)
for k, v in enumerate(ranking):
	print('O {} ficou em {}  lugar'.format(v[0], k+1))
