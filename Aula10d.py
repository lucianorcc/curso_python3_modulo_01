n1 = float(input('Entre com a 1ª nota: '))
n2 = float(input('Entre com a 2ª nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Parabéns! Você foi aprovado com média {:.1f}.'.format(media))
else:
    print('Infelizmente, você foi reprovado :(. Sua média foi {:.1f}.'.format(media))