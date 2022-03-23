'''Crie um programa onde o usuario possa digitar varios valores numaricos e cadastreos em uma lista.
Caso o numero já exista la dentro ele não sera adicionado. No final mostre todos os valores
únicos digitados, em ordem cresente.'''


lista = []
while True:
    v = 0
    num = int(input('Digite um valor:'))
    for n in lista:
        if n == num:
            v += 1
    if v == 0:
        lista.append(num)
        print('Sucesso em adicionar digito!')
    else:
        print('Falha ao adicionar digito!')
    while True:
        sair = str(input('Gostaria de continuar? S/N')).upper().strip()
        if sair != 'S' and sair != 'N':
            print('Resposta invalida! Tente novamente.')
        else:
            break
    if sair == 'N':
        break
lista.sort()
print(f' Os valores digitados foram {lista}')

