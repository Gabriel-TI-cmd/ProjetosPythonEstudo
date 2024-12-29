s = 0
v = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        s += n
        v += 1
print('A soma do(s) {} valore(s) solicitado(s), que são pares, é {}'.format(v, s))
