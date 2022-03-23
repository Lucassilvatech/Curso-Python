'''Ler varios numeros inteiros. O programa so vai parar quando o usuario digitar o valor 999. No final mostre quantos
numeros foram digitados e qual a soma entre eles. 'Desconsidere o frag' '''
'''l = 0
n = 0
h = 0
while n != 999:
    n = int(input('digite um valor'))
    if n != 999:
        k = str(input('Gostaria de continuar? Responda com S para sim e N para não.')).lower()
    if n != 999:
        h = h + 1
        l = l + n
    if k == 's':
        n = n
    elif k == 'n':
        n = 999
print(f'Você digitou {h} numeros e a soma entre eles é de {l} .')'''
soma = cont = n = 0
while n != 999:
    n = int(input('Digite um valor: [ 999 para sair].'))
    if n != 999:
        soma += n
        cont += 1
print(f'foram digitados {cont} numeros e a soma entre eles é {soma}')

