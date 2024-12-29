num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das opções de conversão:
[ 1 ] Binário;
[ 2 ] Octal;
[ 3 ] Hexadecimal.''')
escolha = int(input('Opção: '))
if escolha == 1:
    print('O valor {} convertido para BINÁRIO é igual {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O valor {} convertido para OCTAL é igual {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O valor {} convertido para HEXADECIMAL é igual {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
