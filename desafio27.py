nome=input("Digite seu nome completo: ").strip()
divisa=nome.lower().split() #divide a string em uma lista de palavras (o separador padrão é o espaço em branco) e converte a string para minúsculas
print("Seu primeiro nome é {}" .format(divisa[0])) #imprime a primeira palavra da lista
print("Seu último nome é {}" .format(divisa[-1])) #imprime a última palavra da lista

#!Outra forma de fazer sem criar a variável divisa

nome=input("Digite seu nome completo: ").strip()
print("Seu primeiro nome é {}" .format(nome[0])) #imprime a primeira palavra da lista
print("Seu último nome é {}" .format(nome[len(nome)-1])) #imprime a última palavra da lista 