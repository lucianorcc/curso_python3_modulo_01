salario = float(input('Digite o salário: '))
if salario > 1200:
    novosalario = salario + (salario * 10 / 100)
    print('Salário de R$ {:.2f}. Após 10% de reajuste ficou em R$ {:.2f}.'.format(salario, novosalario))
else:
    novosalario = salario + (salario * 15 / 100)
    print('Salário de R$ {:.2f}. Após 15% de reajuste ficou em R$ {:.2f}.'.format(salario, novosalario))