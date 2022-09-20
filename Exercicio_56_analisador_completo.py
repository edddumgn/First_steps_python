cont_idade = 0
c_idade_maior = 0
c_nome_maior = ''
media_idade = 0
mulher20 = 0
for pessoa in range(1,5):
	print('-'*5,'{}* PESSOA'.format(pessoa),'-'*5)
	nome = str(input('Nome: ')).strip().lower()
	idade = int(input('Idade: '))
	sexo = str(input('Sexo [M/F]: ')).upper().strip()
	media_idade += idade
	if pessoa == 1 and sexo in 'Mm':
		c_idade_maior = idade
		c_nome_maior = nome
		
	elif sexo in 'Mm' and idade > c_idade_maior:
		c_idade_maior = idade
		c_nome_maior = nome
		
	if sexo in 'Ff' and idade < 20:
		mulher20 += 1
		
		
print('A media de idade do grupo é de {}!'.format(media_idade/4))
print('O homem mais velho tem {} anos e se chama {}!'.format(c_idade_maior, c_nome_maior.title()))
print('{} mulheres tem menos de 20 anos!'.format(mulher20))


