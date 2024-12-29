'''
C = str(input('Em que cidade você nasceu? ')).strip()
Up = C.upper()
Ver = 'SANTO' in Up
print('Essa cidade tem o nome "SANTO"? {}'.format(Ver))
'''
C = str(input('Em que cidade você nasceu? ')).strip()
print('Essa cidade tem o nome "SANTO"? {}'.format('SANTO' in C.upper()))
