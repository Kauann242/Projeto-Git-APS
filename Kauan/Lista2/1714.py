#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

venda = float(input(""))
venda_ = 0

if venda < 20:
    bonus = venda * 0.45
    venda_ = venda + bonus
else:
    bonus = venda * 0.3
    venda_ = venda + bonus

print("Valor de venda: R$%.2f" %(venda_))