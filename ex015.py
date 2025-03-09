d = int(input('quantos dias o carro foi alugado: '))
km = float(input('quantos km rodados: '))
total = (d * 60) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(total))