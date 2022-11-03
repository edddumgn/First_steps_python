
def fatorial(num,show=False):
	f = 1
	if show == False:
		for n in range(1,num+1):
			f *= n
		print(f)
	
	elif show == True:
		for n in range(1,num+1):
			f *= n
			if n < num: 
				print(f'{n} X ',end='')
			elif n == num:
				print(f'{num} = ',end='')
				print(f'{f}')


fatorial(5,True)
		
