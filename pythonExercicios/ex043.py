## Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
'''
1) à vista dinheiro/cheque: 10% de desconto;
2) à vista no cartão: 5% de desconto;
3) em até 2x no cartão: preço normal;
4) 3x ou mais no cartão: 20% de juros;
'''

print("{:=^40}".format(" LOJAS GSM "))
p = float(input("Preço das compras: (R$) "))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] À vista dinheiro/cheque")
print("[ 2 ] À vista no cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
cp = int(input("Qual é a opção? "))
if cp == 1:
    np = p - (p * 10/100)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final. ".format(p, np))
elif cp == 2:
    np = p - (p * 5/100)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(p, np))
elif cp == 3:
    np = (p / 2)
    print("São duas parcelas de R${:.2f} SEM JUROS.".format(np))
elif cp == 4:
    parcelas = int(input("Quantas parcelas? "))
    p_parcela = (p / parcelas)
    p_parcela_juros = (p_parcela * 20 / 100) + p_parcela
    np = (p_parcela_juros * parcelas)
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS.".format(parcelas, p_parcela_juros))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(p, np))
else:
    print("Opção INVÁLIDA de pagamento. Tente novamente!")
