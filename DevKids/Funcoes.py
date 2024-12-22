def nome_funcao():
	"""Exibe uma saudação."""
	print("Hello")
nome_funcao()


def hello_user(nome ="joao",sobrenome = "silva"):
	"""Exibe uma saudação com um nome e sobrenome""" #Doc string
	print("Hello {} {}".format(nome,sobrenome))
hello_user("Eduardo","Magno") #Argumento posicional

hello_user(sobrenome ="Magno", nome = "Eduardo") #Argumento nomeado

hello_user() #Argumento default


def soma(a=0,b=0,c=0):  #Função retornando valores
	"""Soma 3 números"""
	s=a+b+c
	return s 
r1=soma(2,3,5)
r2=soma(1,1)
r3=soma(8)
print("As somas deram {}, {}, {}".format(r1,r2,r3))
