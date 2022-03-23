'''Tem que perguntar a distancia de uma viagem em km e calcular o preço da passagem, cobrando R$0,50 por Km para
viagens de ate 200Km e R$0,45 para viagens mais longas'''


'''km = float(input('Qual a distância da viagem que quer fazer:'))
if km > 200:
    print(f'O valor da passagem vai ser R${km * 0.45:.2f}')
else:
    print(f'O valor da passagem vai ser R${km * 0.50:.2f}')'''

# uma outra forma de fazer:
km = float(input('Qual a distancia da viagem:'))
preso = km * 0.50 if km <= 200 else km * 0.45
print(f'O valor da passagem vai ser R${preso}')