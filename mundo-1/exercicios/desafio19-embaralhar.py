from random import shuffle

nome1 = str(input('Informe o nome do PRIMEIRO aluno: '));
nome2 = str(input('Informe o nome do SEGUNDO aluno: '));
nome3 = str(input('Informe o nome do TERCEIRO aluno: '));
nome4 = str(input('Informe o nome do QUARTO aluno: '));

lista = [nome1, nome2, nome3, nome4];
embaralhar = shuffle(lista)

print('A ordem de apresentação será:\n{}'.format(lista));