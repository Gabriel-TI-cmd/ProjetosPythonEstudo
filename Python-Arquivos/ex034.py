s = float(input('Qual é o salário do funcionário? R$'))
if s > 1250:
    a = (s * 10/100) + s
else:
    a = (s * 15/100) + s
print('Quem ganhava um salário de R${:.2f} passa a ganhar R${:.2f} agora.'.format(s, a))
