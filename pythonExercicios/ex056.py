genero = str(input('Informe o seu gênero: [M/F] ')).strip().upper()[0]
while genero not in 'MF':
    genero = str(input('Dados inválidos. Favor, tente novamente: [M/F] ')).strip().upper()[0]
print('Gênero {} registrado com sucesso!'.format(genero))
