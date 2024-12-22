#programa que epde numero inteiro entre 0 e 60 e depois mostra a mensagem:"O numero informado foi: "
numero_inteiro = int(input("Digite um número inteiro entre 0 e 60: "))
if numero_inteiro <0:
	print("número inválido")
elif numero_inteiro > 60:
	print("número inválido")
else:
	print("O numero informado foi {}".format(numero_inteiro))

 
