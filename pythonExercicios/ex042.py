from time import sleep

print('-=' * 20)
print('CÁLCULO DE IMC')
print('-=' * 20)
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está com o PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA! Cuidado!')
print('-=' * 20)
print('FIM')
print('-=' * 20)
print('AVISO: O programa fechará em 30 segundos após o resultado.')
sleep(30)
