print('-=' * 20)
print(' ' * 9, 'É UM NÚMERO PRIMO?')
print('-=' * 20)
n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='') ## Amarelo;
        tot += 1
    else:
        print('\033[31m', end='') ## Vermelho;
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi dividido {} vezes.'.format(n, tot))
if tot == 2:
    print('Por isso ele É PRIMO.')
else:
    print('Por isso ele NÃO É PRIMO.')
