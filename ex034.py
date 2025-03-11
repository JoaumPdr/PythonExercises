salario = float(input('Qual o salario do funcionario em R$? '))
aumento = float

if salario >= 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15
print('Quem ganhava {:.2f} agora passa a ganhar R${:.2f}'.format(salario, aumento))
