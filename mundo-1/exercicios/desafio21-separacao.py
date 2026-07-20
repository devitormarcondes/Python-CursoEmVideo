numero = int(input('Informe um número: '));
unidade = numero % 10 
dezena = (numero //10) % 10
centena = (numero //100) % 10
milhar = (numero //1000) % 10

print('Analisando o número {}...'.format(numero));
print('Unidade: {}\nDezena: {}\nCentena:\n{}Milhar: {}'.format(unidade, dezena, centena, milhar))
