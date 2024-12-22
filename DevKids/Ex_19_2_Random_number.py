from random import randint

computador = randint(0,10)
jogador = int(input("Pensei em um número entre 0 e 10, tente adivinhar..\n"))
if computador == jogador:
	print("Você ganhou!")
else:
	print("Você errou! Pensei no número {}".format(computador))
