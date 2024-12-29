'''
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
data_atual = date.today()
print('A data atual é: {}'.format(data_atual))
if ano == 0:
    ano_atual = date.today().year
    if ano_atual % 4 == 0:
        print('O ano atual {} é bissexto.'.format(ano_atual))
elif ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 == 0:
        print('O ano {} é bissexto.'.format(ano))
    elif ano % 100 == 0 or ano % 400 == 0:
        print('O ano {} não é bissexto.'.format(ano))
    else:
        print('O ano {} é bissexto.'.format(ano)) # Aqui são só os bissextos divisíveis por 4.
else:
    print('O ano {} não é bissexto.'.format(ano))
'''
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
