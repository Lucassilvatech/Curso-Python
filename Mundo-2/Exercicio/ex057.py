'''Ler o sexo de uma pessoa, mas só aceite os valores 'M' e 'F' .
Caso esteja errado , peça a digitação novamente até ter um valor correto.'''

n = ''
while n != 'F' and n != 'M':
    n = str(input('Qual o seu sexo?[M/F]')).upper().strip()
    if n != 'M'and n != 'F':
        print('Opição invalida, digite novamente')
print('sexo M resistrado com sucesso')