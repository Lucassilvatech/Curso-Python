n = input('digite algo:')
print(('È um espaço?'), bool(n.isspace()))
print(('È alpha numerico?'), bool(n.isalnum()))
print(('È um numero?'), bool(n.isnumeric()))
print(('Alphabeto?'), bool(n.isalpha()))
print(('È letra minuscula?'), bool(n.islower()))
print(type(n))