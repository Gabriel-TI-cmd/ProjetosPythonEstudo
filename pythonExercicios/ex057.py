res = str(input('Quer iniciar? [S/N] ')).strip().upper()[0]
soma = qtd_num = media = maior = menor = 0
num_lista = list()
while res == 'S':
    num = int(input('Digite um número: '))
    qtd_num += 1
    soma += num
    num_lista.append(num)
    if num > maior:
        maior = num
    if qtd_num > 1:
        menor = min(num_lista)
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        media = soma / qtd_num
        print('A média dos valores mencionados é {:.1f}'.format(media))
        print('O maior valor de entrada foi {}'.format(maior))
        print('O menor valor de entrada foi {}'.format(menor))
        break
print('FIM')
