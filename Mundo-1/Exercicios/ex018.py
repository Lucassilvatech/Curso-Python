'''import math
angulo = float(input('digite um angulo:'))
s = math.sin(angulo)
t = math.tan(angulo)
c = math.cos(angulo)
print(f'O valor de seno é {s:.2f}\nO valor da tangente é {t:.2f}\nO valor do cosseno é {c:.2f}')'''


import math
angulo = float(input('digite um valor em angulo:'))
s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
print(f'O valor do seno é {s:.2f} \nO valor do cosseno é {c:.2f} \nO valor da tangente é {t:.2f}')
