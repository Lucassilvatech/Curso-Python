'''calcular o aumento no salario de um funcionario
 Para salarios superiores a R$1.250,00, calcule um almento de 10%.
 Para os inferiores ou iguais, o almento é de 15%'''

salario = float(input('Digite o valor do seu salario para um reajuste:'))
if salario <= 1250:
    n = salario * (15 / 100)
    n = n + salario
    print(f'Seu salario com o reajuste de 15% fica R${n} .')
else:
    n1 = salario * (10 /100 )
    n1 = n1 + salario
    print(f'Seu salario com o reajuste de 10% fica R${n1} .')
