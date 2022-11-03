from datetime import datetime
cadastro = dict()
current_year = datetime.now().year
cadastro['nome'] = str(input('Nome: ')).strip()
cadastro['ano'] = int(input('Ano: '))
cadastro['cdt'] = int(input('Carteira de Trabalho (0 não tem): '))

if cadastro['cdt'] != 0:
	cadastro['adc'] = int(input('Ano de Contratação: '))
	cadastro['salario']= str(input('Salário: '))
	print('-='*30)
	for k, v in cadastro.items():
		print('-{} tem o valor {}'.format(k,v))
	print('-idade é',current_year-cadastro['ano'],'anos')

elif cadastro['cdt'] == 0:
	print('-='*30)
	for k, v in cadastro.items():
		print('-{} tem o valor {}'.format(k,v))
	
