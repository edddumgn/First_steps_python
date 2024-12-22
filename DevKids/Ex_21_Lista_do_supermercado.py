lista = []
num_item = 1

while(True):
	item = input("Qual o {}° item:\n".format(num_item))
	num_item = num_item + 1
	
	if item == "fim":
		print("Aqui esta a sua lista")
		break
	else:
		lista.append(item)
print(lista)
		
		
