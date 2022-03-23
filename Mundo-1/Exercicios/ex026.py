''' tem que ler uma frase qualquer e mostrar:
- quantas vezes aparece a letra 'a'.
 - Em que posição aparece pela primeira vez.
 - Em que posição ela aparece pela ultima vez.'''

frase = str(input('Escreva um frase qualquer:').strip())
frase = frase.lower()
frase = frase.replace('ã','a')
frase = frase.replace('á','a')
frase = frase.replace('â', 'a')
n = frase.count('a')
ai =int(frase.find('a')) + 1
af = int(frase.rfind('a')) + 1
print(f'Essa frase tem um total de {len(frase)} caracteres.')
print(f'Essa frase tem {n} letras "a" \n'
      f'A letra "a" aparece pela primeira vez na posição {ai} \n'
      f'e aparece pela ultima vez na posição {af} ')