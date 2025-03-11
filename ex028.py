from random import randint
from time import sleep

computador = randint(0,5)
print('Pensei em um numero entre 0 e 5, será que você consegue advinhar?')
escolha = int(input('Digite um numero entre 0 e 5: '))
print('Processando...')
sleep(2)
if escolha == computador:
    print('PARABENS VOCE ACERTOU!!')
else:
    print('GANHEI! eu pensei no numero {} e nao no {}'.format(computador, escolha))