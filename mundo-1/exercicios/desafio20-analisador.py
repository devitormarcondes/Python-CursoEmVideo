nome_completo = str(input('Informe o seu nome completo: '));
nome_maisculo = nome_completo.upper()
nome_minusculo = nome_completo.lower()
primeiro_nome = nome_completo.split()

print('Análisando seu nome....\nNome com letras maíusculas: {}\nNome com letras minusculas: {}'.format(nome_maisculo, nome_minusculo))
print('Seu nome tem ao todo {} letras'.format(len(nome_completo) - nome_completo.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro_nome[0], len(primeiro_nome)))