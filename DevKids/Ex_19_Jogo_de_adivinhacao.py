
import random
num_computador = random.randint(0,10)
print("O computador está pensando em um número!")
print("Pense em um número entre 0 e 10")
num_pessoa = int(input("Tente adivinhar o número que o computador pensou: "))
print("O computador pensou no número {}.".format(num_computador))
print("Você digitou o número {}.".format(num_pessoa))
if num_computador == num_pessoa:
	print("Você acertou!")
else:
	print("Que pena, você errou!")
