num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

x = num1
y = num1

if num2 > x:
	x = num2
if num3 > x:
	x = num3

if num2 < y:
	y = num2
if num3 < y:
	y = num3

print("O maior número digitado foi {} e o menor foi {}".format(x,y))
