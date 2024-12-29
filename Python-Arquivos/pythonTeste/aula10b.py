carro = int(input('Qual é o ano de seu carro? '))
idade = 2024 - carro
if idade >= 3:
    print('O seu carro tem {} ano(s).'.format(idade))
    print('O carro é velho.')
else:
    print('O seu carro tem {} ano(s).'.format(idade))
    print('O carro é novo.')
