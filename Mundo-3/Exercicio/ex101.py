'''Crie um programa que tenha uma função chamada voto() que vai receber como parametro
o ano de nascimento de uma pessoa, retornando um valor literal indicamdo se uma pessoa tem voto NEGADO,
OPCIONAL ou OBRIGATORIO nas eleições.'''

from datetime import date

def voto (ano):
    atual_ano = date.today().year
    idade = atual_ano - ano
    if idade <= 15:
        return "NEGADO"
    if 15 < idade < 18 or idade >= 65:
        return "OPICIONAL"
    if 18 <= idade <= 64:
        return "OBRIGATÓRIO"


#programa principal
resu = voto(int(input('Digite seu ano de nascimento:')))
print(resu)