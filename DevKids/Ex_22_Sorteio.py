pessoas = []
qnt_pessoas = int(input("Quantas pessoas serão sorteadas?\n"))


for i in range(qnt_pessoas):
	selecionados = input("Qual o nome da {}º pessoa?".format(i+1))
	pessoas.append(selecionados)
	
	import random
escolhido = random.choice(pessoas)
print("Ganhador é {}".format(escolhido))

#Outra maneira de fazer:	
#print("A pessoa escolhida foi:\n{}".format(random.choice(pessoas)))

