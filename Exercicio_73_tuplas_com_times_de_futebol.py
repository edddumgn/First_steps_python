campeonato = ('Corinthians','Palmeiras','Santos','Gremio',
'Cruzeiro', 'Flamengo','Vasco','Chapecoence','Atletico','Botafogo',
'Atletico-PR','Bahia','São Paulo','Fluminense','Sport Recife', 'EC Vitoria',
'Curitiba','Avai','Ponte Preta', 'Atletico-GO')
print('-='*20)
print(f'Lista dos times do Brasileirão: {campeonato}')
print('-='*20)
print(len(campeonato))
print('*Os cinco primeiros são ',end='')

for time in range(0,5):
	print(campeonato[time] ,end=' ')
print(f'\n *Os cinco primeiros são {campeonato[:5]}')

print('-='*20)
print(f'*Os quatro ultimos são {campeonato[-4:]}')
print('-='*20)
print(f'*Times em ordem alfabetica {sorted(campeonato)}')

print('-'*20)
print(f'Chapecoence está na {campeonato.index("Chapecoence")+1} posição.') #Não é possivel usar aspas dentro de aspas no 'f por isso o uso de aspas duplas
