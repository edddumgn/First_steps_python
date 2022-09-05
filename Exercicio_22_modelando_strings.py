nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome ...')
#Nome em letras maiusculas
print('Seu nome em maiusculas é: {}.'.format(nome.upper()))
#Nome em letras minusculas
print('Seu nome em minusculas é: {}.'.format(nome.lower()))
#Quantas letras tem no nome sem os espaços
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
#Quantas letras tem o primeiro nome
print('Seu primeiro nome tem {} letras.'.format(nome.find(' '))) 


separa = nome.split()
print('Seu primeiro nome {} tem {} letras.'.format(separa[0],len(separa[0])))
