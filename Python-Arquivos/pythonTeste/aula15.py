idade = salario = 0
nome = ''
while True:
    nome = str(input('Digte o seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    salario = float(input('Digite o seu salário: '))
    print(f'O {nome} tem {idade} anos de idade e ganha R${salario:.2f} por mês, de salário.')
    if (nome != '') and (idade != 0) and (salario != 0):
        break
