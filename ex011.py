a = float(input('a altura da parede é: '))
l = float(input('a largura da parede é: '))
area = a * l
print('a dimensao da sua parede é {}x{} e sua area é {}m2'.format(a, l, area))
tinta = area / 2
print('para pintar essa parede, voce precisara de {}l de tinta'.format(tinta))