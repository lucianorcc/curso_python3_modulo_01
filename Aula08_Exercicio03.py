from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo qualquer: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O SENO do ângulo de {}° é {:.2f}'.format(ang, sen))
print('O COSSENO do ângulo de {}° é {:.2f}'.format(ang, cos))
print('A TANGENTE do ângulo de {}° é {:.2f}'.format(ang, tan))


