'''Criar um programa que leia a idade e sexo de varias pessoas. A cada pessoa cadastada o programa devará perguntar se
 a pessoa quer continuar. No final mostre:
 1) quantas pessoas tem mais de 18 anos
 2) Quantos homens foram cadastrados
 3)Quantas mulheres tem menos de vinte anos'''
soma = soma2 = soma3 = 0
while True:
    sx = com = ''
    print('=' * 35)
    idade = int(input('Qual sua idade?'))
    while sx != 'M'and sx != 'F':
        sx = str(input('Qual o seu sexo? [M/F]')).upper().strip()[0]
        if sx != 'M' and sx != 'F':
            print('\033[31mOPÇÃO INVALIDA, Tente novamente.\033[m')
    if idade > 18:
        soma = soma + 1
    if sx == 'M':
        soma2 = soma2 + 1
    else:
        if idade < 20:
            soma3 = soma3 + 1
    while com != 'M' and com != 'F':
        com = str(input('Gostaria de continuar? [S/N]')).upper().strip()[0]
        if com != 'S' and com != 'M':
            print('\033[31mOPÇÃO INVALIDA, Tente novamente.\033[m')
    if com == 'N':
        break
print(f'No grupo {soma} pessoas tem mais de 18 anos.\n'
      f'No grupo foram cadastrados {soma2} homens.\n'
      f'No grupo {soma3} mulheres tem menos de 20 anos.')
