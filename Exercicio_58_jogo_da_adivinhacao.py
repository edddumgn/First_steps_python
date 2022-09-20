import random
print('Sou seu computador ...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

comp = random.randint(0,10)
print(comp)
n = 11
c = 0
while n != comp:
	n = int(input('Qual é o seu palpite? '))
	c += 1
	if n < comp:
		print('Muito abaixo! Tente outro numero!')
	elif n > comp:
		print(' Muito acima! Tente novamente!')
print('Parabéns! Você acertou!')
print('Você acertou com {} tentativas. Parabéns!!'.format(c))
