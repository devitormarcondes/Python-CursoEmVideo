from random import choice 

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...');
lista = choice ([0,1,2,3,4,5]);
usuario = int(input('Em que número eu pensei? '));
if usuario == lista:
    print('PARÁBENS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {}, e não no {}'.format(lista,usuario))