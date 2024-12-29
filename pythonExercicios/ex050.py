print('=' * 30)
print(' ' * 5, '10 TERMOS DE UMA PA')
print('=' * 30)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dcimo = n1 + (10 - 1) * r
for c in range(n1, dcimo + r, r):
    print('{} '.format(c), end=' -> ')
print('ACABOU')
