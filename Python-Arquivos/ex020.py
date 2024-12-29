'''
from math import sqrt
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = sqrt(oposto ** 2 + adjacente ** 2)
print('A hipotenusa vale {:.2f}'.format(hipotenusa))
'''
from math import hypot
op = float(input('Compriemento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
hi = hypot(op, ad)
print('A hipotenusa vale {:.2f}'.format(hi))
'''
op = float(input('Compriemento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
hi = (op ** 2 + ad ** 2) ** (1/2)
print('A hipotenusa vale {:.2f}'.format(hi))
'''
