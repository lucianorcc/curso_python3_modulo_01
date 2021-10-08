# strip remove os espaços indesejados antes e depois
nomecompleto = str('Paulo de Souza Marques').strip()
nome = nomecompleto.split()[0]
print('Maiuscula: {}'.format(nomecompleto).upper())
print('Minuscula: {}'.format(nomecompleto).lower())
print('Quantidade de Caracteres sem Espaço: {}'.format(len(nomecompleto) - nomecompleto.count(' ')))
print('Quantidade de Caracteres do 1° nome {}: {}'.format(nome, len(nomecompleto)))