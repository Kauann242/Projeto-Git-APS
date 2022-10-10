#https://www.beecrowd.com.br/judge/pt/custom-runs/code/402428
valorInicial = 1000

anoAtual = int(input(''))
anos = anoAtual - 2005

if anoAtual < 2006:
    print('O ano informado deverá ser > 2005!')

else:
    porcentagem = (0.015)
    anoAnterior = valorInicial
    while (anos) > 0:
        calc = anoAnterior + (anoAnterior*porcentagem)
        anoAnterior = calc
        porcentagem = porcentagem + 0.01
        anos = anos -1
    print("Salário atual: R$%.2f"%(calc))