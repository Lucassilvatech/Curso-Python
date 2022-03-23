'''Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- a media da turma
- a situação(opicional)
add tbm as docstrings da função'''

def notas (*nota,stc=False):
    maior = menor = soma = 0
    total_nota = len(nota)
    for pos, valor in enumerate(nota):
        soma = soma + valor
        if pos == 0:
            maior = valor
            menor = valor
        else:
            if maior < valor:
                maior = valor
            if menor > valor:
                menor = valor
    media = soma / total_nota
    if stc == True:
        if media <= 5:
            situacao = 'Ruim'
        elif media < 7:
            situacao = 'Rasoavel'
        elif media >=7:
            situacao = 'Boa'

    situacao = 'Não passada'

    dicionario = {'QuantidadeNotas': total_nota, 'maiorNota': maior, 'menorNota': menor, 'mediaDaTurma': media,'situacao':situacao}

    return dicionario



n = notas(1, 2, 6, 44, 32)
print(n)
