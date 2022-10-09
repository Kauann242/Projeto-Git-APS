#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = input("")
hora_extra = float(input(""))

salario_min = 1192.4
valor_horaExtra = 10

salario_horaExtra = hora_extra * valor_horaExtra
sal_bruto = (3 * salario_min) + salario_horaExtra

if sal_bruto <= 2000:
    inss = sal_bruto * 0.05
    if sal_bruto <= 2500:
        irrf = sal_bruto * 0
    else:
        irrf = sal_bruto * 0.2

else:
    inss = sal_bruto * 0.12
    if sal_bruto <= 2500:
        irrf = sal_bruto * 0
    else:
        irrf = sal_bruto * 0.2
        
descontos = irrf + inss
salario = sal_bruto - descontos
        
print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" %(sal_bruto))
print("Salário líquido: R$%.2f" %(salario))
