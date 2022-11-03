#Básico
try:
	a = int(input('Numerador: '))
	b = int(input('Denominador: '))
	r = a / b
except:
	print('Infelizmente tivemos um problema!')

else:
	print(f'O resultado é {r:.1f}')

finally:
	print('Volte sempre!')

#Básico 1
try:
	a = int(input('Numerador: '))
	b = int(input('Denominador: '))
	r = a / b
except Exception as erro:
	print(f'Infelizmente tivemos um problema! Erro {erro.__class__}')

else:
	print(f'O resultado é {r:.1f}')

finally:
	print('Volte sempre!')
	
#Básico 2
try:
	a = int(input('Numerador: '))
	b = int(input('Denominador: '))
	r = a / b
except (ValueError, TypeError):
	print('Tivemos um problema com os tipos de dados que você digitou.')
except (ZeroDivisionError):
	print('Não é possivel fazer uma divisão por zero.')
except KeyboardInterrupt:
	print('O usuário preferiu não informar os dados')
else:
	print(f'O resultado é {r:.1f}')

finally:
	print('Volte sempre!')
