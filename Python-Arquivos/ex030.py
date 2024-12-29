V = float(input('Qual é a velocidade atual do carro em Km/h? '))
limite = 80
if V > 80:
    print('MULTADO! Você excedeu o limite permitido que é de {}Km/h'.format(limite))
    multa = 7 * (V - limite)
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
