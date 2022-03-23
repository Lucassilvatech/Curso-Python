'''faça o computador jogar jokenpô com vc'''

from random import choice

from time import sleep

print('Qual você escolhe, \033[34mpedra\033[m ,\033[34mpapel\033[m ou \033[34mtesoura\033[m?')

#Vai pegar resposta do jogador
jogador = str(input('\033[33mNão se preocupe estou de olhos fechados.\033[m Digite oque escolheu:')).lower().strip()

#Vai pegar a resposta do computador
maquina = choice( [1, 2, 3])
if maquina == 1:
    maquina = 'pedra'
elif maquina == 2:
    maquina = 'papel'
elif maquina == 3:
    maquina = 'tesoura'

#Vai conferir quem ganhou
if maquina in 'pedra'and jogador in 'papel':
    resultado = 'Você ganhou. Parabéns!!!'

elif maquina in 'tesoura' and jogador in 'pedra':
    resultado = 'Você ganhou. Parabéns!!!'

elif maquina in 'papel' and jogador in 'tesoura':
    resultado = 'Você ganhou. Parabéns!!!'

elif maquina in 'pedra' and jogador in 'tesoura':
    resultado = 'HA HA eu ganhei!! Mais sorte na proxima.'

elif maquina in 'tesoura' and jogador in 'papel':
    resultado = 'HA HA eu ganhei!! Mais sorte na proxima.'

elif maquina in 'papel' and jogador in 'pedra':
    resultado = 'HA HA eu ganhei!! Mais sorte na proxima.'
else:
    resultado = ' Empatamos. Vamos jogar novamente!'

# Comtagem para resultado
print('\033[7;29mPedra...\033[m')
sleep(0.5)
print('\033[7;29mPapel...\033[m')
sleep(0.5)
print('\033[7;29mTesoura...\033[m')
sleep(0.7)

# Resultado
print(f'\033[30mEu escolhi \033[4m{maquina}\033[m \033[30me você \033[4m{jogador}\033[m' )
sleep(0.5)
print(f'\033[4;32m{resultado}\033[m')

