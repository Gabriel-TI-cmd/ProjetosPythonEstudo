from datetime import date
nasc = int(input('Ano de Nascimento: '))
nome = input('Nome do Atleta: ')
ano_atual = date.today().year
idade = ano_atual - nasc
if idade <= 9:
    print('O(A) atleta {} tem classificação MIRIM, com idade de {} anos!'.format(nome, idade))
elif idade <= 14:
    print('O(A) atleta {} tem classificação INFANTIL, com idade de {} anos!'.format(nome, idade))
elif idade <= 19:
    print('O(A) atleta {} tem classificação JÚNIOR, com idade de {} anos!'.format(nome, idade))
elif idade <= 25:
    print('O(A) atleta {} tem classificação SÊNIOR, com idade de {} anos!'.format(nome, idade))
else:
    print('O(A) atleta {} tem classificação MASTER, com idade de {} anos!'.format(nome, idade))

## Poderia ser um else aqui por último, em vez de elif idade > 25;