nome = str(input('Qual é o seu nome:'))
if nome == 'Lucas':
    print('Que nome lindo!')
elif nome == 'Alan':
    print('Alanzoka é você????!')
elif nome == 'João' or nome == 'Pedro' or nome == 'Fabio':
    print('sei lá')
elif nome in 'Alana Juliana Samily Kathia':
    print('Belo nome feminine')
else:
    print('Não é a mamãe!')
print(f'Olá, {nome}!')