import random
from time import sleep
num = random.randint(0,5)
print('processing...')
sleep(3)
print('Huummm...')
sleep(1)
print('Its you will never guess!')
sleep(2)
user = int(input('try to descover the number that the computer thought, between 0 and 5: '))
if user == num:
	print('Congratulations!You got the number right {}!'.format(num))
else:
	print('What a pity, the number was {}.'.format(num))
