info = dict()
gols = list()

info['nome'] = input('Nome do jogador: ')
p = int(input('Quantas partidas {} jogou? '.format(info['nome'])))

for part in range(1,p+1):
	partida = int(input('Quantos gols na partida {}? '.format(part)))
	gols.append(partida)
info['gols'] = gols[:] 


info['tgol'] = sum(gols)
print(gols)
print(info)
print('-='*30)
for k, v in info.items():
	print(f'O campo {k} tem valor {v}')
print('-='*30)

print('O jogador {} jogou {} partidas'.format(info['nome'],p))
for p, g in enumerate(gols):
	print(f'=> Na partida {p}, fez {g} gols')
print('Fez um total de {} gols'.format(info['tgol']))
