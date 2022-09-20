from colorama import init, Fore, Back, Style
init()
num = int(input('Digite um numero: '))

c = 0
for i in range(1,num+1):
	if num % i == 0:
		print('\033[31m',end=' ')
		c += 1
	else:
		print('\033[34m',end=' ')
	print('{}'.format(i),end=' ')
print('\033[37m\nO numero {} foi dividido {} vezes!'.format(num,c))
if c == 2:
	print('O numero {} é primo!'.format(num))
else: 
	print('O numero {} NÃO é primo!'.format(num))
