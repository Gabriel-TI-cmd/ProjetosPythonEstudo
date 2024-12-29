'''
from random import choice
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
lista = [0, 1, 2, 3, 4, 5]
n = choice(lista)
# print(n)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if num == n:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(n, num))
'''

from time import sleep
from random import randint

num = randint(0, 10)
print('-=-' * 20)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10. Tente adivinhar...''')
print('-=-' * 20)
palpites = 0
while True:
    n = int(input('Em que número eu pensei? '))
    palpites += 1
    if num == n:
        print('PROCESSANDO...')
        sleep(2)
        print('Vc acertou o número que pensei, que é {}. Parabéns!'.format(num))
        print(f'Foram {palpites} palpites até acertar.')
        break
    else:
        print('PROCESSANDO...')
        sleep(2)
        if num > n:
            print('Mais... tente mais uma vez.')
        elif num < n:
            print('Menos... tente mais uma vez.')
        sleep(1)
        continue
