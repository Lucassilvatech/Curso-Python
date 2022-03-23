'''Cria um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario quer ou
não continuar. No final mostre:
1) Qual o total gasto na compra
2)quantos produtos custão mais de 1000r$
3) Qual e´o nome do produto mais barato'''

'''val = 0
soma = cont = 0
while True:
    print('='* 38)
    pro = str(input('Nome do produto:'))
    preço = int(input('Preço do produto:'))
    soma += preço
    if preço >= 1000:
        cont += 1
    val += 1
    if val == 1:
        nmenor = pro
        menor = preço
    else:
        if menor > preço:
            nmenor = pro
            menor = preço
    end = ''
    while end != 'S' and end != 'N':
        end = str(input('Gostaria de comtinuar a digitar produtos? [S/N]')).upper().strip()[0]
        if end != 'S' and end != 'N':
            print('\033[31mCOMANDO INCORRETO, Tente novamente!\033[m')
    if end == 'N':
        break
print('=' * 38)
print(f'No total sua compra deu {soma}R$\nTem {cont} produtos custando mil reais ou mais.\n'
      f'O produto mais barato é {nmenor} costando {menor}R$')'''

# pequena diferença da minha solução, reduzindo um nó.

val = 0
soma = cont = 0
while True:
    print('='* 38)
    pro = str(input('Nome do produto:'))
    preço = int(input('Preço do produto:'))
    soma += preço
    if preço >= 1000:
        cont += 1
    val += 1
    if val == 1 or menor > preço:
        nmenor = pro
        menor = preço

    end = ''
    while end != 'S' and end != 'N':
        end = str(input('Gostaria de comtinuar a digitar produtos? [S/N]')).upper().strip()[0]
        if end != 'S' and end != 'N':
            print('\033[31mCOMANDO INCORRETO, Tente novamente!\033[m')
    if end == 'N':
        break
print('=' * 38)
print(f'No total sua compra deu {soma}R$\nTem {cont} produtos custando mil reais ou mais.\n'
      f'O produto mais barato é {nmenor} costando {menor}R$')






