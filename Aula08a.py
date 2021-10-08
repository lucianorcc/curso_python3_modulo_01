from math import sqrt, floor, ceil
num = int(input('Digite um número: '))
# Calculando a Raiz Quadrada
## Comando floor= arredonda para baixo
## Comando ceil = arredonda para cima
raiz = sqrt(num)
print('A Raiz Quadra de {} é {}.'.format(num,raiz))
print('A Raiz Quadra de {} é {}. Arredondo para baixo'.format(num,floor(raiz)))
print('A Raiz Quadra de {} é {}. Arredondo para cima'.format(num,ceil(raiz)))