n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
menor = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
print('O menor valor digitado foi {}'.format(menor))
maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
print('O maior valor digitado foi {}'.format(maior))
'''
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
lista = [n1, n2, n3]
lista.sort()
print(f'O maior valor digitado foi {lista[2]}\nE o menor valor digitado foi {lista[0]}')
'''
