p = float(input('Qual o preço do produto: '))
d = int(input('Qual a porcentagem de desconto: '))
aplicardesconto = p - (p * d / 100)
print('O produto custava {}, na promoção com o desconto de {}% vai custar {:.2f}'.format(p, d, aplicardesconto))