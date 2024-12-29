n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
'''
n = int(input('Digite um número para calcular seu fatorial: '))
f = 1
print('{}! = '.format(n), end='')
while n >= 1:
    f *= n
    if n == 1:
        print('{} '.format(n), end='')
        break
    print('{} x '.format(n), end='')
    n -= 1
if n == 0:
    print(1, end=' ')
print('= {}'.format(f))
'''
# Existe a classe factorial do módulo math que calcula fatorial;
