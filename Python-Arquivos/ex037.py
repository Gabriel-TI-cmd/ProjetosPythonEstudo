casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = float(input('Quantos anos de financiamento? '))
meses = tempo * 12
prestacao = casa / meses
min = ((30/100) * salario)
if prestacao > min:
    print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}'.format(casa, tempo, prestacao))
    print('Empréstimo NEGADO!')
else:
    print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}'.format(casa, tempo, prestacao))
    print('Empréstimo APROVADO!')
