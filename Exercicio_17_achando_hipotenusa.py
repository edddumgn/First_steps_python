import math
catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjascente: '))

hipotenusa = math.sqrt(catop**2 + catad**2)
print('O comprimento da hipotenusa é de {:.2f}.'.format(hipotenusa))


hipotenusa2 = math.hypot(catop, catad)
print('O comprimento da hipotenusa é de {:.2f}!'.format(hipotenusa2))
