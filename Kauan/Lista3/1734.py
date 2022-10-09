#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

N = int(input(""))
fator = N
c = 0

while c < (N - 1):
    fator = fator * (c + 1)
    c += 1
    
print("%i! = %i" %(N, fator))