entrada = input("Digite algo: ")
classe = (type(entrada))

print(f"O tipo primitivo desse valor é {classe}")
print("Só tem espaços?",entrada.isspace())
print("É númerico?",entrada.isnumeric())
print("É alfabetico?",entrada.isalpha())
print("É alfanúmerico?",entrada.isalnum())
print("Está em maiusculas?",entrada.isupper())
print("Está em minúsculas?",entrada.lower())
print("Está capitalizada?",entrada.istitle())

