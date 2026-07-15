from random import choice

aluno1 = str(input('Informe o nome do PRIMEIRO aluno: '));
aluno2 = str(input('Informe o nome do SEGUNDO aluno: '));
aluno3 = str(input('Informe o nome do TERCEIRO aluno: '));
aluno4 = str(input('Informe o nome do QUARTO aluno: '));
alunos = [aluno1,aluno2,aluno3,aluno4];
escolha = choice(alunos);

print('O aluno escolhido foi {}'.format(escolha))