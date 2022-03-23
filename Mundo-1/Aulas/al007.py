# cores no terminal

#codigo anci

# \033[m base do codigo
# \033[0;33;44m valores dentro do codigo base representam,STYLE, TEXT e BACK

# STYLE = Fonte das letras.
# TEXT = Cor do texto.
# BACK = Cor de fundo.

#codigos
'''Style                                    Text          Back'''
     # 0 padrão                                29             40   branco
     # 1 bold 'negrito'                        31             41   vermelho
     # 4 underline 'sublinhar'                 32             42   verde
     # 7 negative 'inverter text com back'     33             43   amarelo
#                                              34             44   azul
#                                              35             45   roxo
#                                              36             46   ciano
#                                              37             47   cinza

print('\033[7;33mOlá, mundo!\033[m')
print('\033[1;31;46mOlá, mundo!\033[m')
print('\033[4;36mOlá, mundo!')
print('\033[4;35mOlá, mundo!')
print('\033[7;30mOlá, mundo!\033[m')
print('\033[7;30mOlá, mundo!')

nome = 'Lucas'
print(f'\033[molá, muinto prazer em te conhecer,\033[36m {nome}\033[m !!!')

