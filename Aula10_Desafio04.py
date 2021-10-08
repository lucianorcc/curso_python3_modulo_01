km = int(input('Digite a dintancia em KM: '))
'''if km <= 200:
    vlr = float(km * 0.50)
else:
    vlr = float(km * 0.45)'''
vlr = km * 0.50 if km <= 200 else km * 0.45 # condição ternária
print('Valor da passagem a pagar: R$ {:.1f}'.format(vlr))
print('----------FIM----------')