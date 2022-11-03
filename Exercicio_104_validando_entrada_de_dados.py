
from colorama import init, Fore, Back, Style
init()

def leiaint(txt):
	while True:
		try:
			print('-' *45)
			n = int(input(txt))
		except (TypeError, ValueError):
			print('\033[31;40m ERRO! Digite um número inteiro válido.\033[m')
			continue
		except KeyboardInterrupt:
			print('Entrada de dados interrompida pelo usuário')	 
			return 0
			break 
		else:
			print(f'\033[32m Você digitou o número {n}\033[m')		  
			return n 
			break
		#finally:
			#print('\033[32m Tenha um bom dia!\033[m')  
				   

n = leiaint('Digite um número: ') 

