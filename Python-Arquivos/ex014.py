p = float(input('Qual é o preço do produto? R$'))
vista = p - (10/100 * p)
pr = p + (8/100 * p)
print('O produto, que custa R${:.2f}, vai valer à vista R${:.2f}'.format(p, vista))
print('O produto, que custa R${:.2f}, vai valer à prazo R${:.2f}'.format(p, pr))
    