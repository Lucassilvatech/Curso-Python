''' O programa tem que ler um numero inteiro qualquer e pedir para o usuario esculher qual será a base de comverção
- 1 para binario
- 2 para octal
- 3 para hexadecimal'''

n = int(input('digite um valor:'))
print('''Escolha um opção para a converção do valor 
{ 1 } para Binario
{ 2 } para Octal
{ 3 } para Hexadecimal''')
v = int(input('imforme a opção desejada  aqui:'))

if v == 1:
    print(f' O valor decimal de {n} para BINÁRIO fica {bin (n)[2:]}')
elif v == 2:
    print(f' O valor decimal de {n} para OCTAL fica {oct (n)[2:]}')
elif v == 3:
    print(f' O valor decimal de {n} para HEXADECIMAL fica {hex (n)[2:]}')