peso_lista = list()
for pess in range(1, 6):
    peso = float(input('{}º Pessoa) Digite seu peso: '.format(pess)))
    peso_lista.append(peso)
peso_menor = min(peso_lista)
peso_maior = max(peso_lista)
print('O maior peso mencionado foi: {:.1f} Kg'.format(peso_maior))
print('O menor peso mencionado foi: {:.1f} Kg'.format(peso_menor))
