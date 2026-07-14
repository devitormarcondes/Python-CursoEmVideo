var = input('Digite qualquer coisa: ');

print('O tipo de variável é: {}'.format(type(var)));
print('Existem apenas números: {}'.format(var.isnumeric()));
print('Existem apenas letras: {}'.format(var.isalpha()));
print('Existem apenas letras e números: {}'.format(var.isalnum()));
print('Possui espaços em branco: {}'.format(var.isspace()));
print('Todas as letras estão em maiúsculo: {}'.format(var.isupper()));
print('Todas as letras estão em minúsculo: {}'.format(var.islower()));
print('Palavra inicia com letra mauiúscula: {}'.format(var.istitle()));
