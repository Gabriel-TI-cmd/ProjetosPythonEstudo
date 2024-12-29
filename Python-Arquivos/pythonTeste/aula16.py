lanche = ('hambúrguer', 'pastel', 'suco', 'pudim')
print('A tupla acima tem ', len(lanche), 'elementos.')
#for c in range(0, len(lanche)):
#   print(f'Eu comprei {lanche[c]} na posição {c}')
#for c in lanche:
#    print(f'Eu comprei {c}')
for pos, c in enumerate(lanche):
    print(f'Eu comprei {c} na posição {pos}')
print('Gastei tudo em lanche...')
print(sorted(lanche))
print(lanche)
