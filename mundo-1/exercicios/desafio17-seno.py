from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '));
radianos = radians(angulo)
seno = sin(radianos);
cosseno = cos(radianos);
tangente = tan (radianos);

print('O ângulo de {:0.2f} tem o SENO de {:0.2f}'.format(radianos, seno));
print('O ângulo de {:0.2f} tem o COSSENO de {:0.2f}'.format(radianos, cosseno));
print('O ângulo de {:0.2f} tem a TANGENTE de {:0.2f}'.format(radianos, tangente));
