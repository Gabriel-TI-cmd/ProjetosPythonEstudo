'''
from random import sample
nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
nomes = [nome1, nome2, nome3, nome4]
sorteio = sample(nomes, 4)
print(sorteio)
'''
from random import shuffle
nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
nomes = [nome1, nome2, nome3, nome4]
shuffle(nomes)
print('A ordem de apresentação será ')
print(nomes)
    