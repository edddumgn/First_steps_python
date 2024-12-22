prova1 = float(input("Nota da primeira prova: "))
prova2 = float(input("Nota da segunda prova: "))
prova3 = float(input("Nota da terceira prova: "))

peso_primeira_prova = prova1 * 2
peso_segunda_prova = prova2 * 5
peso_terceira_prova =prova3 * 3

media = (peso_primeira_prova + peso_segunda_prova + peso_terceira_prova)/10

print("Sua nota média na disciplina é de: {}".format(media))

