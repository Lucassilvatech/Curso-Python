'''faça umprograma que mostre a taboada de varios numeros, um de cada vez. O programa será interrompido quando o numero
for negativo.'''
'''soma = 1
while True:
    n = int(input('Digite um valor para saber sua taboada:'))
    soma += 1
    if soma >=10:'''

while True:
    print('='* 39)
    n = int(input('Digite um valor para saber sua taboada:'))
    if n < 0:
        break
    for cont in range(1,11):
        print(f'{n} X {cont} = {n*cont}')
print('Obrigado por preferir a IA Karen, até a proxima!')



