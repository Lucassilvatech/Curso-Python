''' O programa tem que aprovar um empréstimo bamcario para a compra de uma casa.
 O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 Depois calcular o valor da prestação mensal, sabemdo que ela não pode ultrapassar 30% do salario ou então o emprestimo
 será negado'''

print('\033[4;34mSIMULADOR DE EMPRESTIMO.\033[m')
vcasa = int(input('Valor da casa:'))
anos = int(input('Em quantas ano deseja pagar:'))
salario = int(input('Qual seu salario:'))

par = vcasa / (anos * 12)
if 30 /100 * salario >= par:
    print('\033[32mPARABÈNS!! Seu emprestimo foi aprovado!\033[m\n')
    print(f'O valor das parcelas ficaram R$\033[4;33m{par:.2f}\033[m')
else:
    print('\033[31mSentimos muito não conseguimos aprovar o emprestimo para você.\033[m ')
