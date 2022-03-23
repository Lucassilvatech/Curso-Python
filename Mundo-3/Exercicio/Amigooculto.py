
import random
import os
import time

contador = 0
acumulador = []
resultado = []
part = []
copia = []
print('-'*34)
print('    SORTEADOR DE AMIGO OCULTO!')
print('-'*34)
quantidade = int(input('Digite quantas pessoas vão participar , (O VALOR DEVE SER MAIOR QUE 3):'))
print('-'*34)
# vai pegar o nome dos participantes.
for cont in range(0, quantidade):
    nomes = str(input(f'Digite o nome da {cont + 1}ª pessoa :')).strip().capitalize()
    part.append(nomes)
copia = part[:]
# vai fazer o sorteio.
while True:
    random.shuffle(part)
    random.shuffle(copia)
    n = random.randint(0, len(copia))
    # filtrar erro . Evitar que fique o mesmo nome nas duas listas
    if len(copia) == 2:

        part = sorted(part)
        copia = sorted(copia)
        v = part[1]
        p = part[0]

        if copia[0] == p or copia[1] == v:

            acumulador.append(copia[0])
            acumulador.append(part[1])
            resultado.append(acumulador[:])
            acumulador.clear()
            copia.pop(0)
            part.pop(1)

        elif copia[1] == p or copia[0] == v:
            acumulador.append(copia[0])
            acumulador.append(part[0])
            resultado.append(acumulador[:])
            acumulador.clear()
            copia.pop(0)
            part.pop(0)
        elif copia[n - 1] != part[n - 1]:
            acumulador.append(copia[n - 1])
            acumulador.append(part[n - 1])
            resultado.append(acumulador[:])
            acumulador.clear()
            copia.pop(n - 1)
            part.pop(n - 1)

    elif copia[n - 1] != part[n - 1]:
        acumulador.append(copia[n - 1])
        acumulador.append(part[n - 1])
        resultado.append(acumulador[:])
        acumulador.clear()
        if len(copia) != 0:
            copia.pop(n - 1)
            part.pop(n - 1)
    # Quando não tiver mais participentes na lista o laço para
    if len(copia) == 0:
        break
sair = 0

while True:
    cont = 0
    print('-' * 34)
    # Vai perguntar o nome do participante para mostrar quem ele tirou
    saber = str(input('Digite seu nome para saber quem você tirou :')).strip().capitalize()
    for pos, pess in enumerate(resultado):
        if saber == pess[0]:
            cont = 1
            print(f'Você tirou {pess[1]}')
            print('O RESULTADO SÓ SERA EXIBIDO POR 6 SEC')
            time.sleep(6)
            # apaga o terminal logo apos mostrar quem cada participante tirou
            os.system('cls')
    if cont != 1:
        print('Nome não encontrado! Tente novamente.')
    else:
        # finaliza o programa se "todos" os participantes ja tiverem pego  o resultado
        while True:
            print('-' * 34)
            # retorna erro se a resposta for diferente de sim/s ou não/n, não faz diferença
            # se foi digitado em maiusculo ou minusculo. Se a resposta for não, retorna para o
            # laço for, caso contrario finaliza o programa.
            sair = str(input('Todos os participantes já sabem quem eles tiraram? [S/N] ')).strip().upper()[0]
            if sair not in 'SN':
                print('RESPOSTA INVALIDA. Tente novamente! Digite somente Sim ou Não.')
            else:
                break
        if sair == 'S':
            break
print('-' * 34)
print('Obrigado por usar nossos serviços!')
time.sleep(3)
print('AAh, não dê meia para o amiguinho ^-^')
time.sleep(3)
