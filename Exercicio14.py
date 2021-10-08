c = float(input('Digite a temperatura em grau °C: '))
f = c * 1.8 + 32
print('{}° Celsius equivale {:.2f}° em Fahrenheit.' .format(c, f))
print('='*40)
f = float(input('Digite a temperatura em grau °F: '))
c = (f - 32) / 1.8
print('{}° Fahrenheit equivale {:.2f}° em Celsius.' .format(f, c))