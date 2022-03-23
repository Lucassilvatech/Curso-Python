'''ler varios numeros inteiros pelo teclado. No final da execução , mostre a média entre todos os valores e qual foi o
 maior valor e o menor valor lido. O programa deve perguntar ao usuario se ele quer ou não continuar a
 digitar os valores .'''
n = 0
r = ''
k = 0
cont = 0
while r != 'N':
    r = ''
    n = int(input('Digite um valor:'))
    k = k + n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if menor > n:
            menor = n
        if maior < n:
            maior = n
    while r != 'S' and r != 'N':
        r = str(input('Goataria de continuar? Responda com S para sim e N para não .')).upper().strip()[0]
        if r != 'S' and r != 'N':
            print('\033[31mCOMANDO INCORRETO! Tente novamente.\033[m')


print(f'A media entre os valores foi de {k /cont} o maior numero foi {maior} e o menor foi {menor} ')






