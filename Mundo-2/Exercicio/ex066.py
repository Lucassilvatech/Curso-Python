''''Criar um programa que leia um numero pelo teclado. o programa so vai parar quando o usuario digitar 999.
no final mostre quantos digitos foram digitados e qual a soma entre eles.'''
cont = soma = 0
while True:
    n = int(input('Digite um valor:[999 para parar]'))
    if n != 999:
        cont += 1
        soma += n
    else:
        break
print(f' você digitou {cont} numeros e a soma entre eles é {soma}.')