original = float(input('Qual é o preço orginal do produto? R$ '));
desconto = original * (5/100);
p_desconto = original - desconto;

print('O produto que custava R$ {}, na promoçaõ com desconto de 5% irá ter o novo preço de R$ {}.'.format(original, p_desconto))