dias = int(input('Qual a quantidade de dias que você alugou o automóvel? '));
quilometros = float(input('Quantos quilometros você rodou com o automóvel? '));
preco_dias = dias * 60;
preco_quilometros = quilometros * 0.15;
preco_aluguel = preco_dias + preco_quilometros;

print('O preço total a pagar pelo aluguel do automóvel é de R$ {:0.2f}'.format(preco_aluguel))