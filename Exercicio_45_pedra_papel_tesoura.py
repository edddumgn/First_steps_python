import random
print('R - Rock, P - Paper, or S - Scissors')
user = input('Qual a sua jogada? ').lower()
comp = random.choice(['r','p','s'])

print('You = {}'.format(user))
print('Computer = {}'.format(comp))

if user == 'r' and comp == 'p':
	print('Computer won')
elif user == 'r' and comp == 's':
	print('You won')
elif user == 'p' and comp == 'r':
	print('You wons')
elif user == 'p' and comp == 's':
	print('Computer won')
elif user == 's' and comp == 'r':
	print('Computer won')
elif user == 's' and comp == 'p':
	print(' You won') 

elif user == comp:
	print('tie')
