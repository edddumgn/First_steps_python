valor = float(input("Digite um valor: "))

if valor < 0:
	print("O valor {} é negativo".format(valor))
elif valor >=0:
	print("O valor {} é positivo".format(valor))
else:
	print("Inválido")
