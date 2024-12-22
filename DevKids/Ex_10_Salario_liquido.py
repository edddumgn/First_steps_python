
ganho_hora = float(input("Quanto você ganha por hora: "))
hora_trabalhada = float(input("Quantas horas você trabalha por mês: "))

salario_bruto = (ganho_hora * hora_trabalhada)
print("Salário bruto mensal é de R$ {:.2f}".format(salario_bruto))

imposto_de_renda = (salario_bruto) * 0.11
print("Valor do imposto de renda R$ {:.2f}".format(imposto_de_renda))

inss = salario_bruto * 0.08
print("Valor do inss R$ {:.2f}".format(inss))

sindicato = (salario_bruto * 0.05)
print("Valor do sindicado R$ {:.2f}".format(sindicato))

salario_liquido = (salario_bruto) - (imposto_de_renda) - (inss) - (sindicato)
print("Seu salário líquido é de R$ {:.2f}".format(salario_liquido))
