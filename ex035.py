r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1 or r1 == r2 == r3:
    print('As retas formam um triangulo')
else:
    print('As retas nao formam um triangulo')