extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
  'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
  
while True:
	num = int(input('Digite um numero entre 0 e 20: '))
	if 0<= num <= 20:
		print(f'O numero digitado foi {extenso[num]}')
		continuar = str(input('Deseja continuar? ')).strip().upper()[0]
		if continuar in 'N':
			break
	else:
		print('Tente novamente.', end='')
