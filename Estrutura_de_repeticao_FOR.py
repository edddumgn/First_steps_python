for oi in range(0,6): #Vai de 0 até 5 
	print('Oi')
print('FIM')

for c in range(1,7):#vai do 1 até o 6
	print(c)

for i in range (6,0,-1): #vai de 6 até 1
	print(i)


num = int(input('Digite um numero: '))
for i in range(1,num+1):
	print(i)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for n in range(i,f,p):
	print(n)
	
s = 0
for c in range(0,4):
	n = int(input('Digite um numero: '))
	s += n
print('O somatório de todos os valores foi {}!'.format(s))
