lista_temp = list()
lista_princ = list()
c_pessoas = 0
while True:
	
	nome = lista_temp.append(str(input('Digite seu nome: ')))
	peso = lista_temp.append(float(input('Digite seu peso: ')))
	c_pessoas += 1
	lista_princ.append(lista_temp[:])
	lista_temp.clear()
	continuar = str(input('Quer continuar[S/N]? ')).lower()
	
	while continuar not in 'SsNn':
			continuar = str(input('Quer continuar[S/N]? ')).lower()

	if continuar in 'Nn':
		break
print(f'{c_pessoas} foram cadastradas')

lista_tupla = list()
for lista in lista_princ:
	lista_tupla.append(tuple(lista[:]))
print(lista_tupla)
lista_tupla.sort(key = lambda x: x[1])
print(f'A ordem de pessoas por peso crescente é {lista_tupla}')
lista_tupla.sort(key = lambda x: x[1],reverse = True)
print(f'A ordem de pessoas por peso decrescente é {lista_tupla}')

	

	
	
	
