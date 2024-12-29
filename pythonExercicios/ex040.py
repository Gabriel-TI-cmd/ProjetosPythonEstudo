nome = input('Qual é o nome do aluno? ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('O aluno(a) {} foi REPROVADO(A) com média {:.1f}.'.format(nome, m))
elif m >= 5.0 and m <= 6.9:
    print('O aluno(a) {} ficou de RECUPERAÇÃO com média {:.1f}.'.format(nome, m))
elif m >= 7.0:
    print('O aluno(a) {} foi APROVADO(A) com média {:.1f}.'.format(nome, m))
