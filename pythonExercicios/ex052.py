from datetime import date
ano_atual = date.today().year
pessoa_maior = 0
pessoa_menor = 0
for pess in range(1, 8):
    ano_nasc = int(input('{}º) Digite o ano de seu nascimento: '.format(pess)))
    idade = ano_atual - ano_nasc
    if idade < 18:
        pessoa_menor += 1
    else:
        pessoa_maior += 1
print('Número de pessoas que ainda não atingiram a maioridade: {}'.format(pessoa_menor))
print('Número de pessoas que já atingiram a maioridade: {}'.format(pessoa_maior))
