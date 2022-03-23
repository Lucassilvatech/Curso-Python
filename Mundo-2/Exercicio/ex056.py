'''Ler o nome, idade e sexo de 4 pessoas. No final mostre:
- A media da idadede do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos'''
p = 0
k = 0
j = 0
for c in range(0,4):
    print('====================')
    i = int(input('Qual sua idade?'))
    n = str(input('Qual o seu nome?'))
    s = str(input('Qual o seu sexo [M/F]?')).lower()
    p = p + i
    if s in 'Mm' and i > j:
        l = n
    elif s in 'Ff' and i < 20:
        k = k + 1
    j = i
p = p / 4

print(f'O homem mais velho é {l} \nA quantidade de mulher com menos de 20 é {k} \ne á media da idade do grupo é {p}')
