print('=' * 30)
print('LOJA CEQUESABE')
print('=' * 30)
total = qtd_mil = menor = 0
lista_precos = list()
lista_produtos = dict()
produto_barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço do produto: R$ '))
    lista_precos.append(preco)
    lista_produtos.setdefault(preco, produto)
    total += preco
    if preco > 1000:
        qtd_mil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        menor = min(lista_precos)
        produto_barato = lista_produtos.get(menor)
        break
print('=' * 53)
print('Total gasto na compra: R${:.2f}'.format(total))
print(f'O total de produtos que custam mais de R$1000.00 é: {qtd_mil}')
print('O produto mais barato é {} e custa R${:.2f}'.format(produto_barato, menor))
