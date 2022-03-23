# LISTAS

num = [1,3,5,2]
num[2] = 9
#print(num)# = [1, 3, 9, 2], troca um ele mento por outro

num.append(4)
#print(num)# [1, 3, 9, 2, 4], adiciona um elemento no final da lista

num.sort()
#print(num)# [1, 2, 3, 4, 9], coloca os elementos em ordem
#num.sort(reverse=True)#, coloca na ordem reversa

num.insert(2,0)
#print(num)# [1, 2, 0, 3, 4, 9]# adiciona um valor na posição indicada

num.pop()
#print(num)# [1, 2, 0, 3, 4] remove o ultimo valor da lista se estiver vaziu,
# ou pode remover um valor de uma posição indicada. EX num.pop[2] removeria o 0

num.remove(3)
#print(num)# [1, 2, 0, 4], remove o elemendo indicado, se o elemento não existir na lista da erro

'''valores = []
valores.append(2)
valores.append(7)
valores.append(3)
for cont, v in enumerate(valores):
    print(f'Na posição {cont} encontrei o valor {v}')
   # Na posição 0 encontrei o valor 2 , dá a posição e nome do elemento
   # Na posição 1 encontrei o valor 7
   # Na posição 2 encontrei o valor 3'''

valores = []
for c in range(0,5):
    valores.append(int(input('Digite um valor:')))
for cont, v in enumerate(valores):
    print(f'Na posição {cont} encontrei o valor {v}')

a =[2, 3, 4, 7]
#b = a # cria uma ligação entre as listas, tudo que for alterado em uma vai ser alterado na outra
b = a[:]# dessa forma b vira uma nova lista sem ligação com a

a.append(7)
a.insert(4,5)
print(a)
