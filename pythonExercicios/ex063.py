print('=' * 30)
print(' ' * 5, 'Gerador de PA')
print('=' * 30)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = n1
c = 1
cont = 0
while c <= 10:
    print('{}'.format(t), end=' -> ')
    t += r
    c += 1
    cont += 1
print('STOP')
res = str(input('\nQuer mostrar mais termos? [S/N] ')).strip().upper()[0]
while res == 'S':
    if res == 'S':
        res2 = int(input('Quantos termos? '))
        while res2 != 0:
            print('{}'.format(t), end=' -> ')
            t += r
            res2 -= 1
            cont += 1
        print('STOP')
        res = str(input('\nQuer mostrar mais termos? [S/N] ')).strip().upper()[0]
        continue
print(f'A progressão foi finalizada com {cont} termos mostrados.')
