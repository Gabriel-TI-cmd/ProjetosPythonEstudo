a = (1, 2, 3)
b = (5, 1, 1)
c = a + b
print(f'A tupla c tem {len(c)} elementos. E o elemento 1 aparece {c.count(1)} vezes.')
print(c.index(1, 4))
#  del(c) Esse método apaga a tupla c; Obs: Não posso apagar um elemento ou parte da tupla, e sim ela toda, porque tuplas são imutáveis;
print(c)
