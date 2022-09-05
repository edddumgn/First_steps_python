conta = 4**3
conta2 = pow(4,3) #Função de potencia, porem perde a ordem de precedencia
conta3 = 81**(1/2) #Raiz quadrada = elevar a meio
conta4 = 'Oi' + 'Ola'
conta5 = 'Oi'*5
conta6 = '='*10

nome = input('Digite seu nome: ')
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))

di = num1 // num2
e = num1 ** num2
d = num1 / num2

print(conta)
print(conta2)
print(conta3)
print(conta4)
print(conta5)
print(conta6)
print('A \n divisão\n {:.3f}'.format(d),end="  ")
print('A soma vale {}!'.format(conta+conta2),end='')
print('A divisão inteira {} e a potencia {}'.format(di,e),end='>>')

print('Prazer em te conhecer {:20}!!!!'.format(nome))
print('Prazer em te conhecer {:>20}!!!!'.format(nome))
print('Prazer em te conhecer {:^20}!!!!'.format(nome))
print('Prazer em te conhecer {:=^20}!!!!'.format(nome))
