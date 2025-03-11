v = int(input('Qual a velocidade do seu carro? '))
multa = (v - 80) * 7
if v > 80:
    print('VOCE FOI MULTADO! voce excedeu o limite permitido! que é de 80km/h')
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
    print('Tenha um bom dia! Dirija com segurança.')
else:
    print('Tenha um bom dia! Dirija com segurança.')