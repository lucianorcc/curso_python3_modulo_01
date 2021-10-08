import random
from time import sleep

p = random.randint(0, 5)
print('Eu acabei de pensar em um número. Tente advinhar!')
print('------------------------------------------------')
n = int(input('Qual foi o número que pensei entre 0 e 5? '))
print('AGUARDE.......')
sleep(3)
if p == n:
    print('PRABENS!!! Você acertou... Eu pensei no número {}.'.format(p))
else:
    print('QUE PENA!!! Você errou... Eu NÃO pensei no número {}. Eu pensei no {}'.format(n, p))

