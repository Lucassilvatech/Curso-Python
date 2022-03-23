'''Escreva um programa que leia a velocidade de um carro e se ele utrapassar 80km/h, mostre uma mensagem de que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite'''

km = int(input('Velocidade do carro:'))
if km > 80:
    n = (km - 80) * 7
    print(f'Você tem uma multa de R${n:.2f}. São cobrados R$7.00 por cada km acima do limite de 80km')
print('Diriga com cuidado e respeite os limites de velocida!')
