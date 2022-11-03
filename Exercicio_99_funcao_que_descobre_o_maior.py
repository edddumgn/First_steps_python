

def param(* args):
	maior = 0
	for arg in args:
		if arg > maior:
			maior = arg
	print(maior)

param(53,654,765,867,545,35443,876,56,76,56)
