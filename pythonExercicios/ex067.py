print('=' * 30)
print('ANÁLISE DE DADOS DO GRUPO')
print('=' * 30)

maior = masc = menor_fem = 0
while True:
    idade = int(input('Digite a sua idade: '))
    genero = ' '
    while genero not in 'MF':
        genero = str(input('Digite o seu gênero: [M/F] ')).strip().upper()[0]
    flag = ' '
    while flag not in 'SN':
        flag = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if flag == 'S':
        if idade > 18:
            maior += 1
        if genero == 'M':
            masc += 1
        if genero == 'F':
            if idade < 20:
                menor_fem += 1
    elif flag == 'N':
        break
print('-=' * 48)
print(f'Na lista de cadastro há {maior} pessoas com mais de 18 anos.', end=' ')
print(f'E existem, na mesma, {masc} homens cadastrados.')
print(f'Além disso, há também {menor_fem} mulheres com menos de 20 anos.')
