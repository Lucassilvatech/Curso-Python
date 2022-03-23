'''criar uma tupla com varios produtos e seus respctivos preços, depois organizar tudo em forma tabular'''

produtos = ('caderno', 10.50, 'lapis', 2, 'borracha', 1.50, 'cama', 300, 'smartfone', 500, 'celta',10000)

print('-'*40)
print('LOJINHA DA ONLINE KAREN BOT')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end='')
    else:
        print(f'R$ {produtos[pos]:>6.2f}')
print('-'*40)
