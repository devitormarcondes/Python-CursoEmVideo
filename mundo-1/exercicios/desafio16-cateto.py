from math import hypot

cateto_oposto = float(input('Comprimento do cateto oposto: '));
cateto_adjascente = float(input('Comprimento do cateto adjacente: '));
print('Com o cateto oposto tendo o comprimento de {:0.2f} e o cateto adjascente sendo {:0.2f}, a hipotenusa é {:0.2f}'.format(cateto_oposto, cateto_adjascente, hypot(cateto_oposto,cateto_adjascente)))