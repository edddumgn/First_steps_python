import datetime
ano = int(input('Em que ano você nasceu: '))
atual = datetime.date.today().year
idade = atual - ano
print('Sua idade é {}'.format(idade))


if 2022 - ano <= 9:
	print('Sua categoria é MIRIM')
elif 2022 - ano > 9 and 2022 - ano < 14:
	print('Sua categoria é INFANTIL')
elif 2022 - ano > 14 and 2022 - ano <= 19:
	print('Sua categoria é JUNIOR!')
elif 2022 - ano == 20:
	print('Sua categoria é SÊNIOR')
else:
	print('Sua categoria é MASTER')
