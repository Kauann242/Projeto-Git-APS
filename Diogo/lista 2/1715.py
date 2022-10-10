#https://www.beecrowd.com.br/judge/pt/custom-runs/code/391715
codigo = int(input())
valorT = float(input())

if codigo == 2:
    desconto = (13/100)*valorT
    ValorF = valorT - desconto
    print('Valor total a ser pago: R$%.2f'%ValorF)
elif codigo == 3:
    desconto = (7/100)*valorT
    ValorF = valorT - desconto
    print('Valor total a ser pago: R$%.2f'%ValorF)
elif codigo == 1:
    ValorF = valorT
    print('Valor total a ser pago: R$%.2f'%ValorF)
else:
    print('OPÇÃO INVÁLIDA!')