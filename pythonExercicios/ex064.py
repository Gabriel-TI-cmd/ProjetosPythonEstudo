from time import sleep

soma = cont = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print('Calculando...')
sleep(3)
print('~' * 40)
print(f'A soma dos {cont} números mencionados é: {soma}')
print('~' * 40)
