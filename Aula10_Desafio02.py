v = float(input("Digite a velocidade km/h do carro: "))
if v > 80:
    vlr = float((v - 80) * 7)
    print('SUA VELOCIDADE: {} km/h'.format(v))
    print('VOCÊ ULTRAPASSOU em {} km/h da velocidade permitida de 80 km/h. Multa de R$ {}.'.format(v - 80, vlr))
else:
    print('PARABÉNS!!! Você passou em {} km/h e dentro da velocidade limite de 80 km/h.'.format(v))
