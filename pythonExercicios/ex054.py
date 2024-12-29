print('-=' * 20)
print(' ' * 11, 'É UM PALÍNDROMO?')
print('-=' * 20)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')
'''
print('-=' * 20)
print(' ' * 11, 'É UM PALÍNDROMO?')
print('-=' * 20)
frase = str(input('Digite uma frase: ')).upper().replace(' ', '').strip()
frase_invert = frase[::-1]
frase_count = len(frase_invert)
print('O inverso de {} é {}'.format(frase, frase_invert))
if frase == frase_invert:
    print('A frase digitada É UM PALÍNDROMO.')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO.')
'''
'''
print('-=' * 20)
print(' ' * 11, 'É UM PALÍNDROMO?')
print('-=' * 20)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')
'''
