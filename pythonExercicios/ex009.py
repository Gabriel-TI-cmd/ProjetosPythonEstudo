n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for i in range(1, 11):
    ## res = n * i
    print('{} x {} = {}'.format(n, i, n * i)) ## As operações poderiam ter sido feitas dentro do format;
print('-' * 12)
