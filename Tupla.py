
lanche = ('hamburger', 'suco', 'pizza', 'pudim')
'''
#Tuplas são imutaveis
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[-2:])

for comida in lanche:
	 print(f'Eu comi {comida}')
'''
print(len(lanche))
for cont in range(0,len(lanche)):
	print(f'Eu vou comer {lanche[cont]} na posição {cont}')
	

for pos, comida in enumerate(lanche):
	print(f'Eu vou comer {comida} na posição {pos}')
	
print(sorted(lanche))

a = (2,5,4)
b = (5,8,1,2)
c = a + b 
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(5,2))

pessoa = ('Eduardo', 24, 'M', 50.5)
#del(pessoa) - apaga da memoria a variavel
print(pessoa)
