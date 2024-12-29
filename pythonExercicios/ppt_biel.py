from random import randint
from time import sleep

itens = ['', 'Pedra', 'Papel', 'Tesoura']
print('=' * 11, end='')
print(' JOKENPÔ ', end='')
print('=' * 11)
print('Você tem três opções para jogar:')
print('[ 1 ] Pedra')
print('[ 2 ] Papel')
print('[ 3 ] Tesoura')
print('AVISO: Você está jogando com o computador!')
j1 = int(input('Escolha uma jogada: '))
if j1 > 3 or j1 < 1:
    print('JOGADA INVÁLIDA!')
else:
    sleep(0.5)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!')
    sleep(0.5)
    j2 = randint(1, 3)
    print('=' * 28)
    print('A sua jogada é: {}'.format(itens[j1]))
    print('A jogada do computador é: {}'.format(itens[j2]))
    print('=' * 28)
    if (j1 == 1) and (j2 == 2):
        print('Papel vence pedra, logo, o COMPUTADOR GANHOU!')
    elif (j1 == 2) and (j2 == 3):
        print('Tesoura vence papel, logo, o COMPUTADOR GANHOU!')
    elif (j1 == 3) and (j2 == 1):
        print('Pedra vence tesoura, logo, o COMPUTADOR GANHOU!')
    elif (j1 == 2) and (j2 == 1):
        print('Papel vence pedra, logo, VOCÊ GANHOU!')
    elif (j1 == 3) and (j2 == 2):
        print('Tesoura vence papel, logo, VOCÊ GANHOU!')
    elif (j1 == 1) and (j2 == 3):
        print('Pedra vence tesoura, logo, VOCÊ GANHOU!')
    elif j1 == j2:
        print('EMPATE!')
