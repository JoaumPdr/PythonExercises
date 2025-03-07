s = float(input('Qual o valor do salario: '))
a = int(input('Qual a porcentagem de aumento: '))
aplicaraumento = s + (s * a / 100)
print('Um funcionario que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(s, a, aplicaraumento))
