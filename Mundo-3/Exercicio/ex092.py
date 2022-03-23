'''Crie um programa que leia o nome , ano de nascimento e carteira de trabalho e cadastri-os com idade
em um dicionario se por a caso o ctps for diferente de 0 o dicionario recebera tbm o ano de contratação e o salario
calcule e apresente alem da idade com quantos anos a pessoa vai se aposentar'''

from datetime import date
while True:
    fichario = dict()

    fichario['Nome'] = str(input('Digite o seu nome:'))
    ano = int(input('Em que ano vc nasceu:'))
    idade = date.today().year
    fichario['Idade'] = idade - ano
    fichario['ctps'] = int(input('Digite o numero da sua carteira de trabalho, (0 se não tiver):'))

    if fichario['ctps'] != 0:
        fichario['Contratação'] = int(input('Em que ano foi contratado:'))
        fichario['Salario'] = int(input('Qual o seu salario:'))
        apos = fichario['Contratação'] - ano
        va = idade - apos
        fichario['Aposentadoria'] = idade + 35 - va
    print('-'*35)
    for k, i in fichario.items():
        print(f'{k} tem o valor {i}')
    print('-'*35)
    sair = str(input('Gostaria de continuar? [S/N]'))
    if sair in 'Nn':
        break
