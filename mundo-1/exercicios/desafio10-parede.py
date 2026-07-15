largura = float(input('Largura da parede: '));
altura = float(input('Altura da parede: '));
area = largura*altura;
tinta = area / 2;

print('A sua parede tem a dimensão de {}x{}, e a sua área é de {}M².\nPara pintar totalmente esta parede é necessário {}L de tinta!'.format(largura, altura, area, tinta));