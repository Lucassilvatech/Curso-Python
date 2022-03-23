'''Crie um programa que leia o nome, sexo e idade de varias pessoas guardando os dados de cada
 pessoa em um dicionario e todos os dicionarios em uma lista. No final mostre:
 a) Quantas pessoas foram cadastradas
 b) a media de idade do grupo
 c) uma lista com todas as mulheras
 d) uma lista com todas as pessoas com idadade acima da media'''

quasevelhos = list()
mulheres = list()
lista = list()
while True:
    ficha = dict()
    ficha['Nome'] = str(input('Qual seu nome ?')).strip().capitalize()
    while True:
        ficha['sexo'] = str(input('Qual o seu sexo? [M/F]')).strip().upper()[0]
        if ficha['sexo'] not in 'MF':
            print('ERRO! Digite somente SIM ou NÃO.')
        else:
            break
    ficha['Idade'] = int(input('Qual sua idade?'))
    lista.append(ficha.copy())
    while True:
        sair = str(input('Gustaria de continuar? [S/N]')).strip().upper()[0]
        if sair not in 'SsNn':
            print(' RESPOSTA INVALIDA! Tente novamente.')
        else:
            break
    if sair == 'N':
        break
cont = len(lista)
media = 0
for c in lista:
    for k, i in c.items():
        if k == 'Idade':
            media += i
        if k == 'sexo' and i == 'F':
            mulheres.append(c['Nome'])
media = media / cont
print('-'*35)
print(f'- Foram cadastradas {cont} pessoas .')
print((f'- A media de idade do grupo é {media:.2f}'))
print(f'- As mulheres cadastradas foram {mulheres}')
for ob in lista:
    for chave, it in ob.items():
        if chave == 'Idade' and it > media:
            quasevelhos.append(ob)
for obj in quasevelhos:
    for kay, v in obj.items():
        print(f'{kay} = {v}; ',end='')
    print()
print('>>> PROGRAMA FINALIZADO <<<')

