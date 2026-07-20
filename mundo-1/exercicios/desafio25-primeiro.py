nome_completo = str(input('Digite seu nome completo: '));
nome_completo = nome_completo.strip()
dividido = nome_completo.split()

print('Muito prazer em te conhecer!');
print('Seu primeiro nome é {}.'.format(dividido[0]));
print('Seu último nome é {}.'.format(dividido[-1]));
