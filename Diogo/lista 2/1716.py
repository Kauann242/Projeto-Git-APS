#https://www.beecrowd.com.br/judge/pt/custom-runs/code/391735
codigo = (input())
valorT = float(input())

if codigo == 'A':
    desconto = (10/100)*valorT
    ValorF = valorT + desconto
    print('Novo salário: R$%.2f'%ValorF)
elif codigo == 'B':
    desconto = (15/100)*valorT
    ValorF = valorT + desconto
    print('Novo salário: R$%.2f'%ValorF)
elif codigo == 'C':
    desconto = (20/100)*valorT
    ValorF = valorT + desconto
    print('Novo salário: R$%.2f'%ValorF)
else:
    print('OPÇÃO INVÁLIDA!')