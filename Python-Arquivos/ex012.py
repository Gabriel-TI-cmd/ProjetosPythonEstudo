p = float(input('Qual é o preço do produto? R$'))
p2 = p - (5 / 100 * p)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(p, p2))
