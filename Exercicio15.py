dia = int(input('Quantos dias alugados: '))
km = int(input('Quantos Km rodados: '))
vlrtotal = (dia * 60) + (km * 0.15)
print('O total a pagar é de {:.2f}' .format(vlrtotal))