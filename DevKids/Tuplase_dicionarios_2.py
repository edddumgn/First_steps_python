d = {"x":1,"y":2,"z":5}
d2 = d.copy() #Retorna um outro dicionário com os mesmo intes
d.pop('x') #Remove o item requerido do dicionário
print(d)

d.popitem() #Remove o ultimo item do dicionário

d.clear() #Remove todos os itens do dicionário
print(d)
print(d2)

d["Eduardo"]=200
print(d)
print(d2)

print(d2.items())
print(d2.keys())
print(d2.values())


tpl = (2,3,4,5,6)
print(type(tpl))


