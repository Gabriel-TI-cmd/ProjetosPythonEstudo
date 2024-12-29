dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos quilômetros rodados? '))
valor = (60 * dias) + (0.15 * Km)
print('O preço total de locação do carro, que rodou {}Km e ficou alugado por {} dias, será R${:.2f}'.format(Km, dias, valor))
    