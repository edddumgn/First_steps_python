s = 0
cont = 0
for i in range(1,501,2):	
	if (i % 3) == 0:
		cont = cont + 1 #cont+=1
		s = s + i #s+=i	
print(s)
print('A soma de todos os {} valores é {}'.format(cont, s))

