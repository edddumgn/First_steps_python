salario = float(input('Digite o seu salario: '))
if salario >1250.0:
	reajuste = salario*1.10
	print('O salario será reajustado para {:.2f}!'.format(reajuste))
else:
	reajuste = salario*1.15
	print('O salario será reajustado para {:.2f}!'.format(reajuste))
print('Tenha um bom dia!')
