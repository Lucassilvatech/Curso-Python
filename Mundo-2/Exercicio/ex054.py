'''Ler o ano de nascimenro de 7 pessoas e mostrar quantas delas ja atingiram a maior idade e quantas ainda não'''


from datetime import date
n = date.today().year
k = 0
j = 0
for c in range(1, 8):
    id = int(input('Que ano você nasceu?'))
    l = n - id
    if l >= 21:
        k = k + 1
    else :
        j = j + 1
print(f'{k} pessoas já atingiram a maior idade e {j} ainda não')

