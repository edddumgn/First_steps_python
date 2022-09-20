print('{:=^40}'.format(' LOJAS GUANABARA '))
from colorama import init, Fore, Back, Style
from time import sleep
preco = float(input('Preço do produto :'))
print('Digite: \n 1 - À vista e 2 - À prazo')
init()
modo = int(input('\nModo de pagamento(A vista ou a prazo):  '))

if modo == 1:
	print('Desconto: \n Dinheiro = 10%, Cheque = 10%, Cartão = 5%') 
	modo_2 = input('Será pago em Dinheiro, Cheque ou Cartão? ').upper().strip()
	print('-'*20)
	print('Calculando...')
	print('-'*20)
	if modo_2 == 'DINHEIRO':
			print('O valor a ser pago será de {}!'.format(preco * 0.9))
	if modo_2 == 'Cheque':
			print('O valor a ser pago será de {}!'.format(preco * 0.9))
	if modo_2 == 'CARTÃO' or modo_2 == 'CARTAO':
			print('O valor a ser pago será de {}!'.format(preco * 0.95))
if modo == 2:
	vezes  = int(input('De quantas vezes você quer dividir o pagamento? '))
	if vezes == 2:
		print('O valor total a ser pago será de {}!'.format(preco))
		print('Serão {} parcelas de RS{}!'.format(vezes, preco//2))
	if vezes >= 3:
		print('Em compras parcelas de 3 ou mais vezes há 20% de juros!')
		print('O valor total a ser pago será de RS{}!'.format(preco*1.2))
		print('Serão {} parcelas de RS{}!'.format(vezes, (preco*1.2) // vezes))
else:
	print('\033[31mErro\033[m')
	print('\033[31mOpção invalida!\033[m')
print('Volte sempre!')
