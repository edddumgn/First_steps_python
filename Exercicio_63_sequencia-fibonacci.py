print('-'*30)
print('{:^30}'.format(' SEQUENCIA FIBONACCI '))
print('-'*30)
term = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1

c = 3
print('~'*30)
print('{} -> {}'.format(t1,t2),end=' ')
while c <= term:
	t3 = t2 + t1
	print('-> {}'.format(t3),end=' ')
	t1 = t2
	t2 = t3
	c += 1
print('-> FIM')

