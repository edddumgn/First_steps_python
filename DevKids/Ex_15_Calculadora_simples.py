num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
sinal = input("Digite o sinal: ")

if sinal == "+":
	print(num1 + num2)
elif sinal == "-":
	print(num1 - num2)
elif sinal == "*":
	print(num1 * num2)
elif sinal == "/":
	print(num1 / num2)
else:
	print("	Entrada de dados inválida")

