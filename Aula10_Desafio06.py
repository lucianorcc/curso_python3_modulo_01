num1 = int(input('Entre com o 1º número: '))
num2 = int(input('Entre com o 2º número: '))
num3 = int(input('Entre com o 3º número: '))
# Verificando o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# Verificando o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('maior {}'.format(maior))
print('menor {}'.format(menor))
