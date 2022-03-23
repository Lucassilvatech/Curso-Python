
'''print('-'*30)
print('Olá, mundo')
print('-'*30)
print('-'*30)
print('Aqui é a IA Karen!')
print('-'*30)
print('-'*30)
print('Em que posso ajudar?')
print('-'*30)'''

'''def lin():
    print('-' * 30)


lin()
print('Olá mundo!')
lin()'''

'''def mensagem (msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('Olá, word!')
mensagem('Aqui é a IA Karen!')
mensagem('Vamos nos divertir juntos')'''

'''def soma (a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)


soma(a=2, b=4)
soma(b=9, a=5)
soma(3, 4)'''

'''def contador (*num):
    for c in num:
        print(f'{c}', end=' ')
    print('FIM')


contador(1, 5, 9,)
contador(0, 5)
contador(0, 5, 0, 9, 7)'''

'''def cont (*num):
    tan = len(num)
    print(f' eu encontrei o valor {num} e são ao todo {tan} numeros')


cont(1, 0, 5, 6)
cont(8, 6, 4, 7, 9, 0, 8)
cont(1, 5)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos+= 1


valores = [0, 5, 3, 7, 4, 2]
dobra(valores)
print(valores) # [0, 10, 6, 14, 8, 4]'''

def soma (*num):
    s = 0
    for val in num:
        s += val
    print(f'A soma dos valores é de {s}')


soma(1, 5, 8) #A soma dos valores é de 14
soma(2, 7)    #A soma dos valores é de 9



