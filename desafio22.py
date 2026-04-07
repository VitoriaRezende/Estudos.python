frase = "Vitoria Aparecida Alves Rezende"
print(frase.upper()) #converte a string para maiúsculas
print(frase.lower()) #conver a string para minusculas 
print(len(frase.strip())) #imprime o tamanho da string e remove os espaços em branco no início e no final da string (não altera a string original, apenas retorna uma nova string com os espaços removidos e o tamanho da string)
#quantas letras tem no primeiro nome
print(len(frase.split()[0])) #divide a string em uma lista de palavras e imprime o tamanho da primeira palavra (o separador padrão é o espaço em branco)