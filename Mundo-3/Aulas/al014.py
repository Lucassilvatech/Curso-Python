'''Dicionarios'''
dados = {'Nome':'Lucas','Sexo': 'M','Idade':21}
'''print(dados['Nome'])
print(f'O  nome é {dados["Nome"]} e a idade é {dados["Idade"]}')
print(dados.keys())# dict_keys(['Nome', 'Sexo', 'Idade'])
print(dados.values()) #dict_values(['Lucas', 'M', 21])
print(dados.items()) #dict_items([('Nome', 'Lucas'), ('Sexo', 'M'), ('Idade', 21)])
for k, i in dados.items():
    print(f'{k} = {i}')'''

'''brasil = list()
estado1 = {'uf':'São Paulo', 'sigla':'SP'}
estado2 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil) #[{'uf': 'São Paulo', 'sigla': 'SP'}, {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}]
print(f'{brasil[0]["uf"]}') #São Paulo'''

estado = dict()
brasil = list()
for c in range(0,2):
    estado['uf'] = str(input('Nome do estado:'))
    estado['sigla'] = str(input('Sigla do estado:'))
    brasil.append(estado.copy())# se não for usado o copy cria uma relação entre o dicionario e a lista
    for e in brasil:
        for k, i in e.items():
            print(f'{k} é {i}')
dados['peso'] = 72
print(dados)



