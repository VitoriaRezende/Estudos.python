# Manipulando texto
#? Manipular texto é uma habilidade fundamental em programação. Em Python, existem várias maneiras de trabalhar com strings (sequências de caracteres). Aqui estão algumas operações comuns para manipular texto:
#? 1. Concatenar Strings: Você pode juntar duas ou mais strings usando o operador de adição (+) ou a função join().
#? 2. Fatiar Strings: Você pode acessar partes específicas de uma string usando a notação de fatiamento (slicing) com colchetes [].
#? 3. Substituir Texto: Você pode substituir partes de uma string usando o método replace().
#? 4. Dividir e Juntar Strings: Você pode dividir uma string em uma lista de palavras usando o método split() e juntar uma lista de palavras em uma string usando o método join().
#? 5. Formatar Strings: Você pode formatar strings usando f-strings (disponível a partir do Python 3.6) ou o método format() para inserir variáveis em uma string de maneira mais legível.
#? 6. Manipular Maiúsculas e Minúsculas: Você pode converter uma string para maiúsculas usando o método upper() ou para minúsculas usando o método lower().
#? 7. Verificar Substrings: Você pode verificar se uma substring está presente em uma string usando o operador in ou os métodos find() e index(). exemplo: "Python" in "Curso em Vídeo Python" retorna True, enquanto "Java" in "Curso em Vídeo Python" retorna False. O método find() retorna a posição da primeira ocorrência da substring ou -1 se não for encontrada, enquanto o método index() faz a mesma coisa, mas lança uma exceção se a substring não for encontrada.
#? 8. Contar Caracteres: Você pode contar quantas vezes um caractere ou substring aparece em uma string usando o método count().
#? 9. Remover Espaços: Você pode remover espaços em branco no início e no final de uma string usando o método strip(), ou remover apenas do início com lstrip() ou do final com rstrip().
#? 10. Dividir em Linhas: Você pode dividir uma string em linhas usando o método splitlines() ou juntar uma lista de linhas em uma string usando o método join() com um caractere de nova linha (\n).
#? 11. rfind() e rindex(): Esses métodos são semelhantes a find() e index(), mas procuram a última ocorrência da substring em vez da primeira. O método rfind() retorna a posição da última ocorrência da substring ou -1 se não for encontrada, enquanto o método rindex() faz a mesma coisa, mas lança uma exceção se a substring não for encontrada.
#!------------------------------------------------------------------------------------------------
#fatiamento de string

frase = "Curso em Vídeo Python2"
print(frase)
print(frase[9]) #imprime o caractere na posição 9
print(frase[9:13]) #imprime os caracteres da posição 9 até a posição 12 (o 13 não é incluído - sempre o último número é excluído)
print(frase[9:21]) #imprime os caracteres da posição 9 até a posição 20 (o 21 não é incluído - sempre o último número é excluído)
print(frase[9:21:2]) #imprime os caracteres da posição 9 até a posição 20, pulando de 2 em 2
print(frase[:5]) #imprime os caracteres do início da string até a posição 4 e a mesma coisa que frase[0:5]
print(frase[15:]) #imprime os caracteres da posição 15 até o final da string 
print(frase[9::3]) #imprime os caracteres da posição 9 até o final da string, pulando de 3 em 3
#!------------------------------------------------------------------------------------------------

#analisa de string
frase="Curso em Vídeo Python3"
print(frase.count('o')) #conta quantas vezes a letra 'o' aparece
print(frase.count('o',0,13)) #conta quantas vezes a letra 'o' aparece entre as posições 0 e 12 (o 13 não é incluído - sempre o último número é excluído)
print(frase.find('deo')) #encontra a posição onde começa a sequência 'deo' (se não encontrar, retorna -1)
print(frase.find('Android')) #tenta encontrar a posição onde começa a sequência 'Android' (se não encontrar, retorna -1)
print('Curso' in frase) #verifica se a palavra 'Curso' está presente na string (retorna True ou False)
#len() é uma função que retorna o tamanho da string
print(len(frase)) #imprime o tamanho da string
#!------------------------------------------------------------------------------------------------
#Transformação de string
frase="Curso em Vídeo Python3"
print(frase.replace('Python','Android')) #substitui a palavra 'Python' por 'Android' (não altera a string original, apenas retorna uma nova string com a substituição)
print(frase.upper()) #converte a string para maiúsculas (não altera a string original, apenas retorna uma nova string com a conversão)
print(frase.lower()) #converte a string para minúsculas (não altera a string original, apenas retorna uma nova string com a conversão)
print(frase.capitalize()) #converte a primeira letra da string para maiúscula e o restante para minúsculas ex : Curso em vídeo python3 (não altera a string original, apenas retorna uma nova string com a conversão)
print(frase.title()) #converte a primeira letra de cada palavra para maiúscula e o restante para minúsculas ex: Curso Em Vídeo Python3 (não altera a string original, apenas retorna uma nova string com a conversão)
print(frase.strip()) #remove os espaços em branco no início e no final da string espaços inúteis (não altera a string original, apenas retorna uma nova string com os espaços removidos)
print(frase.rstrip()) #remove os espaços em branco no final da string (não altera a string original, apenas retorna uma nova string com os espaços removidos)
print(frase.lstrip()) #remove os espaços em branco no início da string (não altera a string original, apenas retorna uma nova string com os espaços removidos)
print(frase.upper().count('O')) #converte a string para maiúsculas e conta quantas vezes a letra 'O' aparece (não altera a string original, apenas retorna uma nova string com a conversão e a contagem)
print(frase.lower().find("python")) #converte a string para minúsculas e encontra a posição onde começa a sequência 'python' (se não encontrar, retorna -1) (não altera a string original, apenas retorna uma nova string com a conversão e a busca)
print(len(frase.strip())) #imprime o tamanho da string e remove os espaços em branco no início e no final da string (não altera a string original, apenas retorna uma nova string com os espaços removidos e o tamanho da string)
#!------------------------------------------------------------------------------------------------
#Divisão e junção de string
frase="Curso em Vídeo Python"
print(frase.split()) #divide a string em uma lista de palavras (o separador padrão é o espaço em branco)
print(frase.split('o')) #divide a string em uma lista de palavras usando a letra 'o' como separador ex : ['Curs', ' em Víde', ' Pyth', 'n'] (o separador é a letra 'o' e não é incluído na lista resultante)
print('-'.join(frase)) #junta os caracteres da string usando o caractere '-' como separador (não altera a string original, apenas retorna uma nova string com os caracteres juntados)
print(' '.join(frase)) #junta os caracteres da string usando o caractere ' ' (espaço em branco) como separador (não altera a string original, apenas retorna uma nova string com os caracteres juntados)

