import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo)) 
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O angulo {:.2f}, possui seno {:.2f}, cosseno {:.2f} e tangente {:.2f}!'.format(angulo, seno, cosseno, tangente))

