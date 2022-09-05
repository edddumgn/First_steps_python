frase = 'Curso em video Python'

print(frase[9]) #Mostra o caractere que se encontra na posição 9
print(frase[9:13]) #Mostra os caracteres da posição 9 até a posição 12, a 13 não aparece
print(frase[9:21:2]) #Mostra os caracteres da posição 9 até a posição 20, pulando de 2 em 2
print(frase[:5]) #Mostra os caractere das posição 0 até a 4
print(frase[15:]) #Mostra os caracteres da posição 15 até o final
print(len(frase)) #Conta quantos carecteres há na variavel
print(frase.count('o')) #Conta quantas vezes aparece a letra 'o'
print(frase.count('o',0,13)) #Conta quantos 'o's tem na frase do indice 0 até o indice 12
print(frase.find('deo')) #Mostra em que indice começou a frase 'deo'
print(frase.find('androide')) #Retorna posição -1
print(frase.rfind('o')) #Retorna a posição do 'o' começando da direita
print('Curso' in frase) #Caso tenha a frase na variavel retorna True

#Lista de string é imutavel, só é possivel mexer nela através ds elementos

print(frase.replace('Python','Android'))
print(frase.upper()) #Tudo em letras maiusculas
print(frase.lower()) #Tudo em letras minusculas
print(frase.capitalize()) #Apenas a primeira letra maiuscula, e todas as outras minusculas
print(frase.title()) # Todas as palavras com a primeira letra maiuscula, é identificado atraves dos espaços

frase1 = '   Aprenda Python '
print(frase1.strip()) #Remove todos os espaços no começo e no final da string, o 'A' que era o \n
                       #caractere de indice 3 passa a ser o caractere 0
print(frase.rstrip()) #Strip a direita
print(frase.lstrip()) #Strip a esquerda
print(frase.split()) #Cada palavra vira uma nova string unica
print('-'.join(frase))

print('''Python's convenience has made it the most popular language for machine learning and artificial intelligence. Python's
 flexibility has allowed Anyscale to make ML/AI scalable from laptops to clusters.''')
 
print(frase.lower().find('video'))
