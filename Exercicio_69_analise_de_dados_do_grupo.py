c18 = cm = cf = 0
sexo = continuar = '' 
while True:
	idade = int(input('Qual a sua idade? '))
	sexo = str(input('[M/F]')).upper()[0].strip()
	if sexo != 'M' and sexo != 'F':
		sexo = str(input('[M/F]')).upper()[0].strip()
	continuar = str(input('Quer continuar?[S/N] ')).upper()[0].strip()
	if continuar != 'N' and continuar != 'S':
		continuar = str(input('Quer continuar?[S/N] ')).upper()[0].strip()
	if idade > 18:
		c18 += 1
	if sexo == 'M':
		cm += 1
	if sexo == 'F' and idade < 20:
		cf += 1
	if continuar == 'N':
		break
print(f'{c18} pessoas tem mais de 18 anos!')
print(f'Foram cadastrados {cm} homens!')
print(f'{cf} mulheres tem menos de 20 anos!')
		
		
