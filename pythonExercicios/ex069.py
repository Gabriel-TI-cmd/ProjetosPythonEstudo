print('=' * 30)
print('{:^30}'.format('BANCO USURA'))
print('=' * 30)
valor = int(input('Digite o valor a ser sacado: '))
total = valor
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} células de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO USURA! Tenha um bom dia!')
'''
qtd_cedulas50 = qtd_cedulas20 = qtd_cedulas10 = qtd_cedulas1 = 0
while True:
    saque = int(input('Digite o valor a ser sacado: R$'))
    if saque >= 50:
        qtd_cedulas50 = saque / 50
        print(f'[ 1 ] Total de {qtd_cedulas50:.0f} cédulas de R$50')
    if saque >= 20:
        qtd_cedulas20 = saque / 20
        print(f'[ 2 ] Total de {qtd_cedulas20:.0f} cédulas de R$20')
    if saque >= 10:
        qtd_cedulas10 = saque / 10
        print(f'[ 3 ] Total de {qtd_cedulas10:.0f} cédulas de R$10')
    if saque >= 1:
        qtd_cedulas1 = saque / 1
        print(f'[ 4 ] Total de {qtd_cedulas1:.0f} cédulas de R$1')
    resp = int(input('Escolha uma opção de saque: '))
    match resp:
        case 1:
            print(f'Total de {qtd_cedulas50:.0f} cédulas de R$50 impressas!')
        case 2:
            print(f'Total de {qtd_cedulas20:.0f} cédulas de R$20 impressas!')
        case 3:
            print(f'Total de {qtd_cedulas10:.0f} cédulas de R$10 impressas!')
        case 4:
            print(f'Total de {qtd_cedulas1:.0f} cédulas de R$1 impressas!')
    final = ' '
    while final not in 'SN':
        final = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if final == 'S':
        continue
    elif final == 'N':
        break
'''