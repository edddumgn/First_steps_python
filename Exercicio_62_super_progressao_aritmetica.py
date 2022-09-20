print('{:^40}'.format(' PA GENERATOR '))
print('-='*20)
first_number = int(input('Enter the firt number: '))
ratio = int(input('Enter the ratio: '))

c = 1
pa = first_number
amount = 10
total = 0
print('{} ->'.format(first_number),end=' ')
while amount != 0:	
	total = total + amount
	while c <= total:
		pa += ratio
		c += 1
		print('{} ->'.format(pa),end=' ')
	print('PAUSE')
	amount = int(input('\nHow many ratios do you want to show more? '))
print('In total {} terms were shown.'.format(total)) 
		
			
