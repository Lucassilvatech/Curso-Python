'''Strings'''
'''1- Fatiamento'''
frase = 'Curso em video python'
print(frase[9])# = 'v'. v é o decimo caractere apartir do 0 e esta na posição 9
print(frase[9:13])# = 'vide' v que é o 9 e o é o 12, o 13 e deixado de fora
print(frase[9:21])# = 'video python'
print(frase[9:21:2])# = 'vdopto' vai pular de 2 em 2
print(frase[:5])# = 'Curso'
print(frase[15:])# = 'python'
print(frase[9::3])# = 'veph' vai do caractere 9 até o final pulando de 3 em 3

'''2- Análise'''
print(len(frase))# = '21' conta quantos caracteres ter o texto
print(frase.count('o'))# = '3' conta quantos 'o' tem no texto
print(frase.count('o', 0, 13))# = 1, so tem um 'o'de 0 a 13
print(frase.find('deo'))# = 11, vai mostrar onde começa uma variavel
print(frase.find('android'))# = -1, significa que nao foi encontrada a string no texto
print('Curso'in frase)# = true, segnifica que ele encontrou o elemento no texto
print(frase.replace('python', 'html'))# = curso em video html, troca caracteres. Para salvar a frase alterada
#é presiso atribuir ela a outra variante,EX: l = frase.replace('python','html')
'''3- transfomação'''
print(frase.upper())# = CURSO EM VIDEO PYTHON, transforma as letras minusculas em maiusculas
print(frase.lower())# = curso em video python, deixa tudo em minusculas
print(frase.capitalize())# = Curso em video python, deixa so a primeira letra em maiusculo
print(frase.title())# = Curso Em Video Python, deixa a primeira letra de cada palavra em maiusculo
frase2 = '   aprenda python    '
print(frase2.strip())# = remove espasos do começo e do fim do texto
print(frase2.rstrip())# = remove espasos so da direita do texto
print(frase2.lstrip())# = remove espasos da esquerda

print(frase.split())# = ['Curso', 'em', 'video', 'python'] divide a strig nos espaços, OBS: pesquisar mais a fundo. Aula 9
print('_'.join(frase))# = C_u_r_s_o_ _e_m_ _v_i_d_e_o_ _p_y_t_h_o_n, acresenta um caracterer qualquer entre
# cada letra da strig
print('_'.join(frase.split()))# = Curso_em_video_python, usa a funçao split para acrecentar um carectere qualquer
# entre cada divisao que acontece entre os espaços
print(frase.upper().count('O'))# = 3, upper deixa tudo em maiusculo assim a função count conta quantos desses
# caracteres tem no texto. Logico tambem pode ser usado com o lower para letras minusculas

dividido = frase.split()
print(dividido)# = ['Curso', 'em', 'video', 'python']
print(dividido[0])# = Curso,mostra a primeira palavra, lembrando que a contagem começa do zero
# primeira palavra começa na posição 0 segunda na 1 e assim por diante
print(dividido[2][3])# = 'e' Que é a terceira letra da segunda palavra

