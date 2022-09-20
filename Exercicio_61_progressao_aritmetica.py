print('{:^40}'.format(' PA GENERATOR '))
print('-='*20)

first_number = int(input('Enter the first number: '))
ratio = int(input('Enter the ratio: '))
pa = 0
c = 0

while c != 11:
	pa = first_number + (ratio * c)
	c += 1
	print('{}'.format(pa),end=' ')
	print('->' if c < 11 else '-> THE END',end=' ')

