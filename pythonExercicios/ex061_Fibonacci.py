## Estudante: Gabriel da Silva Machado de Souza;

print('=' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('=' * 30)
n = int(input('Quantos termos você quer na sequência? ')) # Quantidade de termos;
t1 = 0 # Início;
t2 = 1 # Segundo termo;
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='') # Impressão dos dois termos iniciais;
c = 3 # Contador;
while c <= n: # Loop para a impressão do terceiro termo em diante até o limite dado pelo usuário;
    t = t1 + t2 # Soma que gera cada termo da sequência de fibonacci;
    print(' -> {}'.format(t), end='') # Impressão dos termos a partir do terceiro;
    t1 = t2 # Termo anterior ao subsequente;
    t2 = t # Termo subsequente;
    c += 1 # Contagem incrementada em +1;
print(' -> FIM')
print('~' * 30)
