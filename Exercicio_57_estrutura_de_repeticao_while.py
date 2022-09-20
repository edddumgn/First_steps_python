sexo = str(input('Sexo [M/F]: ')).upper()[0].strip()

while sexo != 'F' and sexo != 'M':
	sexo = input('Dados invalidos, por favor informe o seu sexo: ').upper()[0].strip()
print('FIM') 

#OU

while sexo not in 'MmFf':
	sexo = input('Dados invalidos, por favor informe o seu sexo: ').upper()[0].strip()
print('Sexo {} registrado com sucesso!'.format(sexo))
print('FIM')
