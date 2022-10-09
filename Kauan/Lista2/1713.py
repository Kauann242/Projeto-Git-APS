#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valor_hora = float(input(""))
horas = float(input(""))

salario_bruto = valor_hora * horas
irrf = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario = salario_bruto - irrf - inss - sindicato

print("Salário bruto: R$%.2f" %(salario_bruto))
print("Imposto: R$%.2f" %(irrf))
print("INSS: R$%.2f" %(inss))
print("Sindicato: R$%.2f" %(sindicato))
print("Líquido: R$%.2f" %(salario))