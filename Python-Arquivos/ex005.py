nome = input('Qual o nome do aluno? ')
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2)/2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, media))
if media >= 7.0 and media <= 10.0:
    print('O aluno {} está aprovado.'.format(nome))
elif media >= 4.0 and media < 7.0:
    print('O aluno {} está em recuperação!'.format(nome))
else:
    print('O aluno {} está reprovado!'.format(nome))
