info = dict()
list_nome = list()
list_sexo = list()
list_idade = list()
c = 0
c_sexo = 0
while True:
	nome = input('Nome: ')
	c += 1
	list_nome.append(nome)
	sexo = input('Sexo: [M/F]')
	
	while sexo not in 'MmFf':
		print('ERRO! Responda apenas M ou F.')
		sexo = input('Sexo: [M/F]')
	if sexo in 'MmFf':
		list_sexo.append(sexo)
	
	idade = int(input('Idade: '))
	list_idade.append(idade)
	
	continuar = input('Quer continuar? [S/N]').strip().upper()
	if continuar in 'Nn':
		break
	while continuar not in 'NnSs':
		print('ERRO! Por favor, digite apenas S ou N.')	
		continuar = input('Quer continuar? [S/N]').strip().upper()
info['nome'] = list_nome[:]
info['sexo'] = list_sexo[:]
info['idade'] = list_idade[:]
print(info)

print(f'A) Ao todo temos {c} pessoas cadastradas')

print(info['idade'])
print(len(info['idade']))
media = sum(info['idade'])/len(info['idade']) 

print('B) A média de idade é de {:.1f} anos'.format(media))

list_zip = dict(zip(info['nome'],info['sexo']))
print(list_zip)

print('C) As mulheres cadastradas foram',end='')
for k, v in list_zip.items():
	if v in 'Ff':
		print(', {}'.format(k),end='')
	


