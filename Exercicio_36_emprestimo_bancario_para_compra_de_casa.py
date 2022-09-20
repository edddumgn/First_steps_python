print('-'*40)
print('EMPRESTIMO BANCÁRIO PARA COMPRA DE CASA')
print('-'*40)

valor_casa = float(input('Qual o valor da casa:RS '))
salario = float(input('Qual o seu salario: RS'))
anos = int(input('Em quantos anos você pretende pagar: '))

meses = float(anos * 12)
prest_mensal = valor_casa // meses
print(' A prestação será de RS{}!'.format(prest_mensal))
if prest_mensal > (salario*0.3):
	print(' Empréstimo negado!')
elif prest_mensal <= (salario*0.3):
	print('Empréstimo aprovado')
	print('O valor pago mensalmente será de RS{}'.format(prest_mensal))
