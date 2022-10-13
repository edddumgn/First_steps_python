extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
  'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um numero entre 0 e 20: ')) 
while True:
	if num < 0 or num > 20:
		num = int(input('Tente novamente! Digite um numero entre 0 e 20: '))
	
	else:
		for i in range(0,21):
			if i == num:
				print(f'Você digitou o numero {extenso[i]}')
		break
				
			

	
