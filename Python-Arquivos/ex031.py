'''
n = int(input('Me diga um número qualquer: '))
if n % 2 == 0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))
'''
n = int(input('Me diga um número qualquer: '))
res = n % 2
if res == 0:
    print(f'O número {n} é PAR!')
else:
    print(f'O número {n} é ÍMPAR!')
