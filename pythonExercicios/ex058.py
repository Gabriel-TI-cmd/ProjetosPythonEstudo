from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opera = 0
while opera != 5:
    print('''
    Qual operação iniciar?
    [ 1 ] Somar;
    [ 2 ] Multiplicar;
    [ 3 ] Maior;
    [ 4 ] Novos Números;
    [ 5 ] Sair do Programa;
    ''')
    opera = int(input('Operação: '))
    if opera == 1:
        soma = n1 + n2
        print('A soma de {} e {} é: {}'.format(n1, n2, soma))
        break
    elif opera == 2:
        produto = n1 * n2
        print('O produto entre {} e {} é: {}'.format(n1, n2, produto))
        break
    elif opera == 3:
        if n1 > n2:
            maior = n1
            print('O maior valor de entrada é {}'.format(maior))
            break
        elif n2 > n1:
            maior = n2
            print('O maior valor de entrada é {}'.format(maior))
            break
        else:
            print('Os valores {} e {} são iguais.'.format(n1, n2))
            break
    elif opera == 4:
        print('Solicitação para digitar novos valores atendida!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        continue
    elif opera == 5:
        print('Finalizando...')
    elif opera not in [1, 2, 3, 4, 5]:
        print('Dado inválido! Tente novamente.')
        continue
sleep(3)
print('Você saiu do programa. Até breve!')
