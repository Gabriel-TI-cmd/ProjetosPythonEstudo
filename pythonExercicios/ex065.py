while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    else:
        print('-' * 30)
        for c in range(0, 11):
            res = n * c
            print(f'{n} x {c} = {res}')
    print('-' * 30)
print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
