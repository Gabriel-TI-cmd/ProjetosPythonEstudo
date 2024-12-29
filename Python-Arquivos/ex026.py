'''
nome = str(input('Qual é o seu nome completo? ')).strip()
Up = nome.upper()
Ver = 'SILVA' in Up
print('Tem "SILVA" no seu nome completo? {}'.format(Ver))
'''
nome = str(input('Qual é o seu nome completo? ')).strip()
print('O seu nome tem "SILVA"? {}'.format('SILVA' in nome.upper()))
