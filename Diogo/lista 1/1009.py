#https://www.beecrowd.com.br/judge/pt/runs/code/29431049

nome = (input())
salario = float(input())
vendas = float(input())
calc = (((vendas/100)*15)+salario)
print('TOTAL = R$ %.2f'%calc)