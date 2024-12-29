from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno do angulo {} é igual a {:.2f}'.format(angulo, seno))
print('O cosseno do ângulo {} é igual a {:.2f}'.format(angulo, cosseno))
print('A tangente do ângulo {} é igual a {:.2f}'.format(angulo, tangente))
