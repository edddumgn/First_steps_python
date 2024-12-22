lista1 = [1,2,3,4,5]
x1 =len(lista1) #Conta quantos elementos há na lista
print(x1)

print(x1 + 5)
print(min(lista1)) #Retorna o menor valor dentro da lista
print(max(lista1)) #Retorna o maior valor dentro da lista
print(sum(lista1)) #Soma todos os elementos da lista

lista1.append("Eduardo") #Adiciona um elemento ao final da lista
print(lista1)

lista1.insert(1,"Magno") #Insere o elemento na lista,[posição,elemento]
print(lista1) 

lista1.remove(1) #Remove o primeiro elemento indicado
print(lista1)

elemento = "Eduardo"
if elemento in lista1:
	lista1.remove(elemento)
print(lista1)

lista1.pop(2) #Remove o elemento de acordo com o indice, quando o argumento não é informado remove o ultimo elemento
print(lista1)
