print('='*50)
print('{:^50}'.format(' DEZ TERMOS DE UMA PA '))
print('='*50)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

print('{}-->'.format(termo),end='')
for i in range(0,10):
	termo = termo + razao
	print('{}-->'.format(termo),end='')
	
print('ACABOU')
