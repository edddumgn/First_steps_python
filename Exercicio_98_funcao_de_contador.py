
from time import sleep

print('-='*20)
print('  Contagem de 1 até 10 de 1 em 1')
for n in range(1,11):
	sleep(0.1)
	print(' {}'.format(n),end=' ',flush=True)
print('FIM!')

print('\nContagem de 10 até 0 de 2 em 2')
for n in range(10,-1,-2):
	sleep(0.1)
	print(f' {n}',end=' ',flush=True)
print('FIM!')
print('\nAgora é a sua vez!')



def contagem():
	
	ini = int(input('Inicio: '))
	fim = int(input('Fim: '))
	passo = int(input('Passo: '))
	print('-='*20)
	if ini < fim:
		for n in range(ini,fim+1,passo):
			sleep(0.1)
			print(f' {n}',end=' ',flush=True)
	elif fim < ini:
		for n in range(ini,fim,-passo):
			sleep(0.1)
			print(f' {n}',end=' ',flush=True)
	
contagem()
