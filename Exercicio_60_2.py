num = int(input('Digite um numero: '))
f = 1
for i in range(1,num+1):
	f = i * f
print('O fatorial de {} é {}!'.format(num,f))
