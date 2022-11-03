def soma(a,b):
	s = a+b
	print(s)

soma(4,5)
soma(b=10, a=5)


def contador(*num):
	tam = len(num)
	print(f'Recebi os valores {num}, e são ao todo {tam} números')

contador(1,2,3)
contador(0,3)
contador(4,5,7,8,9)


def soma(* num):
	s = 0
	for i in num:
		s += i
	print(s)

soma(2,3)
soma(4,5,6,7)


def dobra(lst):
	pos = 0
	while pos < len(lst):
		lst[pos] *= 2
		pos += 1
	print(lst)

dobra([4,5,6,7])
