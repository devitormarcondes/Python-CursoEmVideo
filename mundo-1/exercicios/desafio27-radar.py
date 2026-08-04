velocidade = float(input('Qual a velocidade atual do carro? '));
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    acima = (velocidade - 80) * 7;
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R$ {:0.2f}'.format(acima));