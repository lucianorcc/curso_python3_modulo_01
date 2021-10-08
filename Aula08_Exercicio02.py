# import math
from math import hypot

ac = float(input('Digite o Cateto Oposto: '))
ab = float(input('Digite o Cateto Adjacente: '))

hi = hypot(ac, ab)

print('O Comprimento da Hipotenusa é: {:.2f}' .format(hi))