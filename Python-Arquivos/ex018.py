'''
import random
alunos = random.randint(1, 4)
print(alunos)
if alunos == 1:
    sorteado = 'Marcos'
    print('{} foi sorteado para apagar o quadro!'.format(sorteado))
elif alunos == 2:
    sorteado = 'Julia'
    print('{} foi sorteada para apagar o quadro!'.format(sorteado))
elif alunos == 3:
    sorteado = 'Carol'
    print('{} foi sorteada para apagar o quadro!'.format(sorteado))
else:
    sorteado = 'Jay'
    print('{} foi sorteado para apagar o quadro!'.format(sorteado))
'''
from random import choice
nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
nomes = [nome1, nome2, nome3, nome4]
sorteio = choice(nomes)
print('O aluno(a) escolhido(a) foi {}.'.format(sorteio))
