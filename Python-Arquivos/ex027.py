'''
frase = str(input('Digite uma frase: ')).strip()
Up = frase.upper()
contar = Up.count('A')
First = Up.find('A')
End = Up.rfind('A')
print('A letra A aparece {} vezes na frase.'.format(contar))
print('A primeira letra A apareceu na posição {}.'.format(First))
print('A última letra A apareceu na posição {}.'.format(End))
'''
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A') + 1))
