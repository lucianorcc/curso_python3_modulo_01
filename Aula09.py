# frase = str(input('Digite uma frase: '))
# print(frase[9:21:2])
# VdoPto
# print(frase[:5])
# Curso
# print(frase[15:])
# Python
# print(frase[9::3])
# Curso em Video Python
# VePh
# print(len(frase))
# print(frase.count('o'))
# 3
# print(frase.count('o', 0, 13))
# 1
# print(frase.find('deo'))
# começou na posicao 11
# print(frase.find('Android'))
# -1 - Nao encontrou nenhuma palavra com nome Android
# print('Curso' in frase)
# Se encontrar a palavra CURSO irá retornar True
# print(frase.replace('Python', 'Luciano'))
# Substituirá a palavra Python por Luciano
# print(frase.upper())
# Passará toda a Frase para MAIUSCULA
# print(frase.lower())
# Passará toda a Frase para MINUSCULA
# print(frase.capitalize())
# Vai deixar apenas a primeira letra da frase em Maiuscula
# print(frase.title())
# Vai deixar cada inicio de palavra da frase com a primeira letra Maiucula
# print(frase.strip())
# remove os espaços inuteis. Ou seja, no inicio e no fim da frase/palavra
#print(frase.rstrip())
# remove os espaços inuteis. Ou seja, no fim da frase/palavra
# print(frase.lstrip())
# remove os espaços inuteis. Ou seja, no inicio da frase/palavra
# print(frase.split())
# ['Curso', 'em', 'Video', 'Python']
# print('-'.join(frase.split()))
# Curso-em-Video-Python
frase = 'Curso em Video Pytho'
dividido = frase.split()
print(dividido[2][3])