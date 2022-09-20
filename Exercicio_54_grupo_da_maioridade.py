from datetime import date
data_atual = date.today().year

c_menor = 0
c_maior = 0

for pessoa in range(1,8):
	ano = int(input('Em que ano a {}* pessoa nasceu? '.format(pessoa)))
	print('Essa pessoa tem {} anos!'.format(data_atual - ano))
	if data_atual - ano >= 18:
		c_maior += 1
	elif data_atual - ano <= 18:
		c_menor += 1
print('Ao todo tivemos {} pessoas maiores de idade!'.format(c_maior))
print('Ao todo tivemos {} pessoas menores de idade!'.format(c_menor))
	
	
