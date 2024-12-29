nome = str(input('Qual é o seu nome? '))
lista_nomes = ['Pedro', 'João', 'Mateus', 'Marcos', 'Bruno']
if nome == 'Gabriel':
    print('Que nome bonito!')
elif nome in 'Ana Marta Marcia Júlia Beatriz Nicoli':
    print('Que belo nome feminino!')
elif nome in lista_nomes:
    print('Seu nome é popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('É uma honra te conhecer. Tenha um bom dia, {}!'.format(nome))
