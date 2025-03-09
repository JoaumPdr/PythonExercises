import math
angulo = float(input('digite o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o seno de {:.2f}\no cesseno de {:.2f}\ne a tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))