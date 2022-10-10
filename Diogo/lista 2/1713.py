#https://www.beecrowd.com.br/judge/pt/custom-runs/code/391671
valorH = float(input())
horasT = int(input())

valorTotal = valorH*horasT

inss = ((8/100)*valorTotal)
impostoRenda = ((11/100)*valorTotal)
sindicato = ((5/100)*valorTotal)
liquido = valorTotal - (inss+impostoRenda+sindicato)
print('Salário bruto: R$%.2f'%valorTotal)
print('Imposto: R$%.2f'%impostoRenda)
print('INSS: R$%.2f'%inss)
print('Sindicato: R$%.2f'%sindicato)
print('Líquido: R$%.2f'%liquido)