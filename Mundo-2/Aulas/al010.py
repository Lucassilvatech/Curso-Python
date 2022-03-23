'''for c in range(1, 10 ):
    print(c)
print('FIN')

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''

# for c in range(1, 3):
#     n = int(input(' digite um valor:'))
# print('FIN')
n = 1
par = im = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            im += 1
print(f' vc digitou {par} numeros pares e {im} numeros impares!')
