n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
i = 0
while i < 10:
    i += 1
    res = n * i
    print('{} x {} = {}'.format(n, i, res))
print('-' * 12)
