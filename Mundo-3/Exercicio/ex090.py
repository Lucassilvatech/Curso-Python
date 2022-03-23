'''faça um programa que leia o nome e media de um aluno,gaurdando tambem a situação em um dicionario
no final mostre o conteudo da estrutura na tela .'''

ficha = dict()
ficha['Nome'] = str(input('Nome do aluno:'))
ficha['Media'] = float(input('Media do aluno:'))
if ficha['Media'] < 5:
    ficha['Situação'] = 'Reprovado(a)'
elif ficha['Media'] < 6.5:
    ficha['Situação'] = 'Recuperação'
else:
    ficha['Situação'] = 'Aprovado(a)'
for k, i in ficha.items():
    print(f'{k} é {i}')
