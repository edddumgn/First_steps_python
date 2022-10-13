soma_par = 0
soma_3 = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
maior = 0
for linha in range(0,3):
	for coluna in range(0,3):
		matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
		if matriz[linha][coluna] %2 ==0:
			soma_par += matriz[linha][coluna]
	
for linha in range(0,3):
	for coluna in range(0,3):
		print(f'[{matriz[linha][coluna]:^5}]',end='')
	print()

for elemento in matriz[linha]:
	soma_3 += elemento		

for elemento in matriz[1]:
	maior = matriz[1][0]
	if elemento > maior:
		maior = elemento
		
print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_3}')
print(f'O maoir valor da segunda linha é {maior}')
