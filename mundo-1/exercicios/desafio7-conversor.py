distancia = float(input('Por favor, insira uma distância em metros: '));
quilometros = distancia / 1000;
hectometros = distancia / 100;
decametros = distancia / 10;
decimetros = distancia * 10;
centimetros = distancia * 100;
milimetros = distancia * 1000;

print('A medida de {}m corresponde a:\n{}Km\n{}Hm\n{}Dam\n{}Dm\n{}Cm\n{}Mm'.format(distancia, quilometros, hectometros, decametros, decimetros, centimetros, milimetros))
