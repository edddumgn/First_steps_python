from random import randint
computador = randint(1,10)
print('Sou seu computador...Acabei de pensar em um numero entre 0 e 10!')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
	jogador = int(input('Qual o seu palpite? '))
	palpites += 1
	if jogador == computador:
		acertou = True
	else:
		if jogador < computador:
			print('Tente um numero mais alto')
		elif jogador > computador:
			print('Tente um numero mais alto')
print('Acertou')
print('Você acertou com {} tentativas'.format(palpites))

