km = float(input('Qual a distancia percorrida? '))
dia = int(input('Quantos dias o carro foi alugado? '))


total = (dia*60) + (km*0.15)
print('O total a pagar sera de {:.2f}!'.format(total))
