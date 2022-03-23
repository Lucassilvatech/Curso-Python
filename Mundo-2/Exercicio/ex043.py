''' O programa tem que ler o peso e altura e calcular o IMC e mostrar seu status
- abaixo 18.5 abaixo do peso
- entre 18.5 e 25 peso ideal
- 25 até 30 sobrepeso
- 30 até 40 obesidade
-acima de 40 obesidade mórbida'''

altura = float(input('Imforme sua altura:'))
peso = float(input('Informe seu peso:'))

imc = peso / altura**2
if imc <= 18.5:
    status = 'Abaixo do peso'
elif imc > 18.5 and imc < 25:
    status = 'Peso ideal '
elif imc >= 25 and imc < 30:
    status = 'Sobrepeso'
elif imc >= 30 and imc <= 40:
    status = 'Obesidade'
else:
    status = 'Obesidade Mórbida'

print(f'Seu IMC foi {imc:.3f} e seu status é:{status}')