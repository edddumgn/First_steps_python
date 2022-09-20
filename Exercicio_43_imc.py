peso = float(input('Digite o seu peso(KG): '))
altura = float(input('Digite sua altura(M): '))

imc = (peso/(altura**2))
print('Seu imc é de {:.1f}'.format(imc))
if imc < 18.5:
	print('Abaixo do peso')
elif 18.5<imc<25:
	print('Peso ideal')
elif 25.0<imc<30:
	print('Sobrepeso')
elif 30<imc<40:
	print('Obesidade')
elif imc>40:
	print('Obesidade Morbida')
