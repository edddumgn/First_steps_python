lista_geral = list()

while True:
	nome = input('Nome: ')
	nota_1 = float(input('Nota 1: '))
	nota_2 = float(input('Nota 2: '))
	media = (nota_1 + nota_2)/2
	lista_geral.append([nome,[nota_1,nota_2],media])
	continuar = str(input('Quer continuar{S/N]? ')).lower()
	
	if continuar in 'Nn':
		break
	while continuar not in 'NnSs':
		continuar = str(input('Quer continuar{S/N]? ')).lower()
		

print('-='*20)
print('No. Nome          MÉDIA')


for posicao, num  in enumerate(lista_geral):
	print(f'{posicao:<4} {num[0]:<10} {num[2]:8.1f}')
	

while True:
	mostrar = int(input('Mostrar as notas de qual aluno?  [999 interrompe] '))
	if mostrar <= len(lista_geral)-1:
		print(f'Notas de {lista_geral[mostrar][0]} são {lista_geral[mostrar][1]}')
	else:
		if mostrar == 999:
			break

