tempo = int(input('Quanto tempo tem seu carro? '))
if tempo <= 3:
	print(f'Seu carro tem apenas {tempo}, esta novo.')
else:
	print('Seu carro já esta velho!')
print('FIM')


print('Carro novo' if tempo <=3 else 'Carro velho')
