'''O programa tem que caucular o valor de um produto considerando as condições de pagamento
- Á vista, 10% de desconto
- Á vista no cartão, 5% de desconto
- Em áte 2x no cartão , preço normal
- 3x ou mais 20% de juros'''

valor = float(input('Valor do produto:'))
print('Qual a forma de pagamento, 1= Á vista, 2= Á vista no cartão, 3= Cartão em 2x ou 4= Cartão em 3x ou mais ')
va =  str(input('Digite aqui a forma de pagamento escolhida :'))

if va in '1':
    v = valor - (10 / 100 * valor )
    print(f'O valor do seu produto ficou R${v:.2f} com desconto de 10%')
elif va in '2':
    v = valor - (5 / 100 * valor )
    print(f'O valor do seu produto ficou R${v:.2f} com desconto de 5%.')
elif va in '3':
    print(f'Vão ficar duas parcelas de R${valor / 2:.2f} sem juros')
elif va in '4':
    p = int(input('quantas vezes?'))
    l = 20 / 100 * valor + valor
    v = l / p
    print(f'Com juros de 20%, o valor do produto ficou R${l:.2f} em {p} vezes de {v:.2f}')

