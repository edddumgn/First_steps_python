numero = int(input("Digite um número: "))

if numero % 2 == 0:
	print("O número {} é par".format(numero))
elif numero % 2 == 1:
	print("O número {} é ímpar".format(numero))
else:
	print("Ínvalido")
