'''Cria um programa que escreva por estenço um numero entre 0 e 20'''
while True:
    while True:
        n = int(input('Digite um valor entre 0 e 20: '))
        if n >= 0 and n <= 20:
            break
        print('OPÇÃO INVALIDA! Tente novamente.',end='')

    valores = ('zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze',
           'Quinze','Desesseis', 'Desessete', 'Dezoito', 'Dezenove', 'Vinte')
    print(f'Você digitou o numero {valores[n]}')
    sair = str(input('Gostariade continuar? S/N')).upper().strip()[0]
    if sair == 'N':
        break
print('Obrigado, volte sempre!')