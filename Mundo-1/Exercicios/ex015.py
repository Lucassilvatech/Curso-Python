a = int(input('Quantos dias o carro ficou alugado?'))
km = int(input('Quantos km rodados?'))
v1 = a * 60
v2 = km * 0.15
vt = v1 + v2
print(f'O valor do aluguel é de {vt:.2f} R$')
