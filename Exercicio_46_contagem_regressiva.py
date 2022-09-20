from time import sleep

print('-='*20)
print('{:^40}'.format(' CONTAGEM REGRESSIVA '))
print('-='*20)
for i in range(10,-1,-1):
	sleep(1)
	print(i)

ja = '*** FOGOS DE ARTIFICIO EXTOURANDO ***'

for i in ja:
	sleep(0.1)
	print(i,end='',flush = True)

