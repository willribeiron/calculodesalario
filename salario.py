"""
Perguntar quanto recebe por hora e quantas horas trabalha no mês. Calcule e mostre o total do salário com os descontos
de 11% por I.R, 8% por INSS e 5% por sindicato.

Mostrar salário bruto
Valor pago INSS
Valor pago sindicato
Valor I.R
Salário liquido

"""
horas_trabalhadas = float(input("Quantas horas você trabalha por mês? "))
salario_hora = float(input("Quanto recebe por hora "))

salario_bruto = salario_hora * horas_trabalhadas

inss = (salario_bruto * 8 / 100)

sindicato = (salario_bruto * 5 / 100)

imposto_renda = (salario_bruto * 11 / 100)

salario_liquido = salario_bruto - inss - sindicato - imposto_renda

print(f"O salário bruto é {salario_bruto}\n O valor do INSS é {inss}\n O valor pago ao sindicato é {sindicato}\n O "
      f"valor pago de I.R é {imposto_renda}\n O salário liquido é {salario_liquido}")

