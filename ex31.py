d = float(input('Qual a distancia da sua viagem? '))
v = float
if d <= 200:
    v = d * 0.50
else:
    v = d * 0.45
print('O valor da sua viagem é de {:.2f}'.format(v))
