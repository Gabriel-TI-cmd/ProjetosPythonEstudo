soma_idade = 0
media_idade = 0
idade_velho = 0
nome_velho = ''
tot_mulher20 = 0
for pess in range(1, 5):
    print('-' * 10, end='')
    print(' {}º Pessoa '.format(pess), end='')
    print('-' * 10)
    nome = str(input('Qual é o seu nome: ')).strip().upper()
    idade = int(input('Qual é a sua idade? '))
    genero = str(input('Qual é o seu gênero [M/F]? ')).strip().upper()
    soma_idade += idade
    if pess == 1 and genero == 'M':
        idade_velho = idade
        nome_velho = nome
    if idade > idade_velho and genero == 'M':
        idade_velho = idade
        nome_velho = nome
    if genero == 'F' and idade < 20:
        tot_mulher20 += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {:.1f} ano(s).'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(idade_velho, nome_velho))
print('Ao todo são {} mulhere(s) com menos de 20 ano(s).'.format(tot_mulher20))
