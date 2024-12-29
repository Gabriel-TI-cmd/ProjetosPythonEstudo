print('='*16)
print('CÁLCULO DA MÉDIA E SITUAÇÃO DO ALUNO.')
print('='*16)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 6.0:
    print('Sua média é {}'.format(m))
    print('PARABÉNS! Você foi aprovado!')
else:
    print('Sua média é {}'.format(m))
    print('ESTUDE MAIS! Você está abaixo da média para ser aprovado!')
print('='*8 + 'FIM' + '='*8)
