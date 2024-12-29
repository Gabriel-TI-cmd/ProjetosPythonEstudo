a = 3
b = 5
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'Branco': '\033[97m',
         'Azul': '\033[34m',
         'Magenta': '\033[35m',
         'Cinza': '\033[37m',
         'Cyan': '\033[36m',
         'Verde': '\033[32m',
         'Preto': '\033[30m',
         'Vermelho': '\033[31m'
}
nome = 'Machado'
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!'.format(a, b))
print('Olá, muito prazer em te conhecer, {}{}{}.'.format(cores['Azul'], nome, cores['limpa']))
'''
text                    background
 
30      black       preto          40
31      red           vermelho   41
32      green       verde         42
33      yellow      amarelo    43
34      blue          azul           44
35      Magenta  Magenta  45
36      cyan         ciano         46
37      grey          cinza         47
97      white        branco     107
'''