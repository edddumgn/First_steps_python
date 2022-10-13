cont1 = 0
cont2 = 0
exp = str(input('Digite sua expressão: '))
for simb in exp:
	if simb == '(':
		cont1 += 1
for simb in exp:
	if simb == ')':
		cont2 += 1
if cont1 == cont2:
	print('A sintaxe de sua expressão é válida!')
else:
	print('expressão com sintaxe inválida!')
