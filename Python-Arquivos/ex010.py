v = float(input('Quanto dinheiro você tem na carteira? R$'))
moeda = input('Escolha a moeda que você quer comprar: US$; euro(€); iene(¥) => ')
print('=' * 37)
if moeda == 'US$':
    dol = 4.90
    convd = v / dol
    print('Com R${:.2f} você pode comprar US${:.2f}'.format(v, convd))
elif moeda == 'euro':
    eur = 5.34
    conve = v / eur
    print('Com R${:.2f} você pode comprar €{:.2f}'.format(v, conve))
elif moeda == 'iene':
    iene = 0.034
    convi = v / iene
    print('Com R${:.2f} você pode comprar ¥{:.2f}'.format(v, convi))
