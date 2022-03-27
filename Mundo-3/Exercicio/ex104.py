'''Crie um programa que tenha uma função chamada leiaint(), que vai funcionar de forma semelhante á função input().
So que agora fazendo a validação para aceitar somente valores numericos.'''

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            ok = True
            valor = int(num)
            return valor
        else:
            print('\033[0;31m[Erro!] Digite um numero inteiro valido.\033[m') 
        if ok == True:
            break
n = leiaint('Digite um numero:')
print(f'Você digitou o numero {n}')
