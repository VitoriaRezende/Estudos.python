#print(type(nome)) # Verifica o tipo da variável nome (str)
#print("não é composta por numeros",nome.isnumeric()) # Verifica se a string é composta apenas por números (False)
#print("é composta somente por letras",nome.isalpha()) # Verifica se a string é composta apenas por letras (True)
#print("é composta por letras e numeros",nome.isalnum()) # Verifica se a string é composta por letras e números (True)
#print("não é composta por espaços",nome.isspace()) # Verifica se a string é composta apenas por espaços (False)
#print("todas as letras são maiusculas",nome.isupper()) # Verifica se todas as letras da string são maiúsculas (False)
#print("todas as letras são minusculas",nome.islower()) # Verifica se todas as letras da string são minúsculas (True)
#print("a primeira letra é maiuscula",nome.istitle()) # Verifica se a primeira letra de cada palavra da string é maiúscula (False)
#print("a string é composta por caracteres imprimiveis",nome.isprintable()) # Verifica se a string é composta por caracteres imprimíveis (True)
#print("a string é composta por caracteres decimais",nome.isdecimal()) # Verifica se a string é composta por caracteres decimais (False)
#print("a string é composta por caracteres digitos",nome.isdigit()) # Verifica se a string é composta por caracteres dígitos (False)
#print("a string é composta por caracteres numericos",nome.isnumeric()) # Verifica se a string é composta por caracteres numéricos (False)   

#Outra forma

nome = input("Digite seu nome: ")

print("Tipo: {}\n" 
      "É numérico? {}\n"
      "É alfabético? {}\n"
      "É alfanumérico? {}\n"
      "Tem apenas espaços? {}\n"
      "Está em maiúsculas? {}\n"
      "Está em minúsculas? {}\n"
      "Está capitalizada? {}\n" 
      "É imprimível? {}\n"
      "É decimal? {}\n"
      "É dígito? {}"
.format(
    type(nome),
    nome.isnumeric(),
    nome.isalpha(),
    nome.isalnum(),
    nome.isspace(),
    nome.isupper(),
    nome.islower(),
    nome.istitle(), 
    nome.isprintable(),
    nome.isdecimal(),
    nome.isdigit()
))
