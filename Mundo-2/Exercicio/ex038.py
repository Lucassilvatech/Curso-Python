''' O programa tem que ler dois valores e mostrar qual deles é maior ou se são iquais'''
'''vl1 = int(input('Digite um valor:'))
vl2 = int(input('Outro:'))
vl = max(vl1, vl2)
if vl1 == vl2:
    vl = 'Não há maior valor, os valores são iguais'
print(f'O maior valor é:{vl}')'''

vl1 = int(input('Digite um valor:'))
vl2 = int(input('Outro:'))
if vl1 > vl2:
    print('o primeiro valor é maior')
    valor =vl1
elif vl2 > vl1:
    print('o segundo valor é maior')
    valor = vl2
elif vl1 == vl2:# tbm poderia ter usado else
    print('as valores são iguais')
'''else :
    valor = 'ab'
if valor == 'ab':
    print(f'Os valores {vl1} e {vl2} são iquais')
else:
    print(f'O maior valor digitado foi {valor}')'''
