primeiro_valor = int(input('Insira o primeiro valor: '));
segundo_valor = int(input('Insira o segundo valor: '));
terceiro_valor = int(input('Insira o terceiro valor: '));

#Verificando MENOR
if primeiro_valor < segundo_valor and primeiro_valor < terceiro_valor:
    print('O MENOR número é o {}'.format(primeiro_valor))
if segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    print('O MENOR número é o {}'.format(segundo_valor))
if terceiro_valor < primeiro_valor and terceiro_valor < segundo_valor:
     print('O MENOR número é o {}'.format(terceiro_valor))

#Verificando MAIOR
if primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
    print('O MAIOR número é o {}'.format(primeiro_valor))
if segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    print('O MAIOR número é o {}'.format(segundo_valor))
if terceiro_valor > primeiro_valor and terceiro_valor > segundo_valor:
     print('O MAIOR número é o {}'.format(terceiro_valor))