nota1 = float(input('Digite a primeira nota: '));
nota2 = float(input('Digite a segunda nota: '));
media = (nota1 + nota2) /2;
print('A sua média do bimestre foi: {:0.1f}'.format(media));
if media >= 6:
    print('O aluno foi APROVADO! Parábens!');
else:
    print('O aluno foi REPROVADO!');
