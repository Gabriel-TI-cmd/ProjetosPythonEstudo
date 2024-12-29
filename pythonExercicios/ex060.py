ni = int(input('Digite um número [999 para parar]: '))  # O 999 é o meu flag;
n = 0
soma = 0
while ni != 999:
    soma += ni
    n += 1
    ni = int(input('Digite um número [999 para parar]: '))
print('O total de números digitados foram: {}'.format(n))
print('A soma de todos esses números é: {}'.format(soma))
