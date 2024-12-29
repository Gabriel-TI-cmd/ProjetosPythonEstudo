'''
nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
first = lista[0]
lista.reverse()
print('Muito prazer em te conhecer!')
print('Primeiro nome: {}'.format(first))
print('Último nome: {}', lista[0])
'''
'''
nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Muito prazer em te conhecer!')
print('O seu primeiro nome é {}.'.format(lista[0]))
print('O seu último nome é {}.'.format(lista[len(lista) - 1]))
'''
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('O seu primeiro nome é {}.'.format(nome[0]))
nome.reverse()
print('O seu último nome é {}.'.format(nome[0]))
