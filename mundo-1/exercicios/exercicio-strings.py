# Fatiamento: exibe os caracteres da string pulando de 2 em 2.
frase = 'Curso em Vídeo Python'
print(frase[::2])

# Conta quantas vezes a letra 'o' aparece na string.
frase = 'Curso em Vídeo Python'
print(frase.count('o'))

# Demonstra que a contagem diferencia letras maiúsculas e minúsculas.
frase = 'Curso em Vídeo Python'
print(frase.count('O'))

# Converte a string para maiúsculas antes de contar a letra 'O'.
frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))

# Retorna o tamanho da string (quantidade de caracteres).
frase = 'Curso em Vídeo Python'
print(len(frase))

# Substitui uma palavra por outra.
frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))

# Verifica se a palavra 'Curso' existe na string.
frase = 'Curso em Vídeo Python'
print('Curso' in frase)

# Retorna a posição onde a palavra 'Vídeo' começa.
frase = 'Curso em Vídeo Python'
print(frase.find('Vídeo'))

# Converte a string para minúsculas e procura pela palavra 'vídeo'.
frase = 'Curso em Vídeo Python'
print(frase.lower().find('vídeo'))

# Divide a string em uma lista de palavras.
frase = 'Curso em Vídeo Python'
print(frase.split())

# Acessa o primeiro elemento da lista gerada pelo split().
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0])

# Acessa um caractere específico dentro de uma palavra da lista.
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])