'''
nome = str(input('Digite seu nome completo: '))
DeleteSpaceEx = nome.strip()
nomeMais = DeleteSpaceEx.upper()
nomeMenos = DeleteSpaceEx.lower()
letrasNum = len(DeleteSpaceEx)
SplitName = DeleteSpaceEx.split()
NomeNotSpace = ''.join(SplitName)
NumLetras = len(NomeNotSpace)
letrasFirstNome = DeleteSpaceEx[0:7]
NumFirstName = len(letrasFirstNome)
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nomeMais))
print('Seu nome em minúsculas é {}'.format(nomeMenos))
print('O nome mencionado sem os espaços tem {} caracteres.'.format(NumLetras))
print('O nome mencionado tem {} caracteres no total.'.format(letrasNum))
print('O primeiro nome tem {} caracteres.'.format(NumFirstName))
'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome)))
print('Seu nome sem os espaços tem {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
