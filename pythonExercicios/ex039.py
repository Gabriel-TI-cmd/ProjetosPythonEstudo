from datetime import date
ano_atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = ano_atual - nasc
print('Quem nasceu em {} tem {} ano(s) em {}.'.format(nasc, idade, ano_atual))
if idade < 18:
    t = 18 - idade
    ano_alist = ano_atual + t
    print('Ainda falta(m) {} ano(s) para o alistamento.'.format(t))
    print(f'Seu alistamento será em {ano_alist}.')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    t = idade - 18
    ano_alist = ano_atual - t
    print('Você já deveria ter se alistado há {} ano(s).'.format(t))
    print(f'Seu alistamento foi em {ano_alist}.')
