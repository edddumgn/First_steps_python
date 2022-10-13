

#Listas - Diferente das Tuplas as Listas podem ser mutáveis

lanche = ['sanduiche', 'suco', 'pizza', 'pudim']
print(lanche)

#adicionar
lanche.append('biscoito')
print(lanche)

lanche.insert(0,'misto')
print(lanche)
'''
#exlcuir
del lanche[3]
lanche.pop() #remove o ultimo elemento
lanche.pop(3)
lanche.remove('pizza') #se tentar remover algo que não esta na lista retorna erro

#então para corrigir o erro de remove:
if 'pizza' in lanche:
	lanche.remove('pizza')
'''

valor = list(range(4,11))
print(valor)

valores = [8,2,5,7,9,1]
print(valores)
valores.sort() #Isso reorganiza a lsita, porem altera a lista original, tem a opção sorted() que não altera a original
print(valores)
valores.sort(reverse=True) #Lista organizada de tras para frente
print(valores)
print(len(valores)) 



num = [2,5,5,7,8]
num.append(7)
print(num)
if 5 in num:
	num.remove(5)
print(num)

lista = []
lista.append(5)
lista.append(7)
lista.append(9)
print(lista)
for c, v in enumerate(lista):
	print(f'Na posição {c} se encontra o valor {v}')

lista1 = []
for cont in range(0,5):
	lista1.append(int(input('Digite um valor: ')))
print(lista1)

a = [2,3,4,7]
b = a   #Se fizer desta maneira pode dar erro, pois o Python
#cria uma ligação entre as duas lista, assim quando mudar algo em b será feita a mudança em 'a' também
#DIFERENTE
b = a[:]

