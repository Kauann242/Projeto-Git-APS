#https://www.beecrowd.com.br/judge/pt/custom-runs/code/391696
n1 = float(input())

if n1 < 20:
    lucro = (45/100)*n1
    valorT = n1 + lucro
else:
    lucro = (30/100)*n1
    valorT = n1 + lucro

print('Valor de venda: R$%.2f'%valorT)