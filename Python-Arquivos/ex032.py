'''
d = float(input('Qual é a distância da sua viagem em Km? '))
print(f'Você está prestes a começar uma viagem de {d} Km')
if d <= 200:
    p = 0.5 * d
else:
    p = 0.45 * d
print('E o preço da sua passagem será: R${:.2f}'.format(p))
'''
d = float(input('Qual é a distância da sua viagem em Km? '))
print(f'Você está prestes a começar uma viagem de {d} Km')
p = d * 0.50 if d <= 200 else d * 0.45
print('E o preço da sua passagem será R${}'.format(p))
