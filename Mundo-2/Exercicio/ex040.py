''' O programa devera calcular a media de um aluno
- média abaixo de 5.0 reprovado
- média entre 5.0 e 6.9 recuperação
 - média 7.0 ou superior aprovado'''

n1 = float(input('Nota 1:'))
n2 = float(input('Nota 2:'))
nota = (n1 + n2) / 2
if nota <= 5.0:
    print(f'Você esta de recuperação. Sua media foi {nota}')
elif nota > 5.0 and nota <= 6.9:
    print(f'Você esta de recuperção. Sua media foi {nota}')
else:
    print(f'APROVADO! Parabéns! Sua media foi {nota}')

