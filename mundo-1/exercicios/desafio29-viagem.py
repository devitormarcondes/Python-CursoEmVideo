viagem = int(input('Qual é a distância da sua viagem? '));
if viagem <= 200:
    passagem = viagem * 0.50;
    print('Você está prestes a começar uma viagem de {:0.2f}'.format(viagem))
    print('O preço da sua passagem será de R$ {:0.2f}'.format(passagem))
else:
    passagem = viagem * 0.45;
    print('Você está prestes a começar uma viagem de {:0.2f}'.format(viagem))
    print('O preço da sua passagem será de R$ {:0.2f}'.format(passagem))