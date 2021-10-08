RED = '\033[1;31m'
BLUE = '\033[1;34m'
CYAN = '\033[1;36m'
GREEN = '\033[0;32m'
RESET = '\033[0;0m'
BOLD = '\033[;1m'
REVERSE = '\033[;7m'
END = '\033[m'

r1 = float(input('Digite a medida da Reta 1: '))
r2 = float(input('Digite a medida da Reta 2: '))
r3 = float(input('Digite a medida da Reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(CYAN + 'Forma um triangulo!' + END)
    if r1 == r2 and r1 == r3:
        print('O Triangulo é Equilátero!')
else:
    print('Não forma um triangulo')
