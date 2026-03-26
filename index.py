# Aspas utilizamos para definir strings, ou seja, textos. Existem três formas de usar aspas em Python:
# 1. Aspas simples (' ')
# 2. Aspas duplas (" ")
# 3. Aspas triplas (''' ''' ou """ """)
# Exemplo de uso de aspas simples:
nome = 'João'
print(nome)  # Saída: João
# Exemplo de uso de aspas duplas:
sobrenome = "Silva"
print(sobrenome)  # Saída: Silva
# Exemplo de uso de aspas triplas:
descricao = '''João é um estudante de Python. Ele gosta de aprender novas linguagens de programação.'''
print(descricao)
# Saída: João é um estudante de Python. Ele gosta de aprender novas linguagens de programação.
# As aspas triplas são especialmente úteis para criar strings que se estendem por várias linhas, como no exemplo acima. Elas também permitem incluir aspas simples e duplas dentro da string
# sem a necessidade de escape, o que pode tornar o código mais legível. Por exemplo:
frase = """Ele disse: "Olá, como vai?" e depois saiu."""
print(frase)  # Saída: Ele disse: "Olá, como vai?" e depois saiu.
# Em resumo, as aspas são usadas para definir strings em Python, e a escolha entre aspas simples, duplas ou triplas depende do contexto e da necessidade de incluir aspas dentro da string.
#o mais usado para definir uma estrinf e as aspas duplas, pois é mais fácil de usar quando precisamos incluir aspas simples dentro da string.
#para imprimir usamos a função print() print("Olá, mundo!")  # Saída: Olá, mundo!

#Uso dos numeros em Python:
#Em Python, os números podem ser representados de várias formas, incluindo inteiros, números de ponto flutuante e números complexos. Aqui estão alguns exemplos de como usar números em Python
# Inteiros
idade = 25
print(idade)  # Saída: 25
# Números de ponto flutuante
altura = 1.75
print(altura)  # Saída: 1.75
# Números complexos
numero_complexo = 2 + 3j
print(numero_complexo)  # Saída: (2+3j) o + é usado também para mostrar duas strings juntas, por exemplo:
print("Olá, " + "mundo!")  # Saída: Olá, mundo
# Operações com números
soma = 10 + 5
print(soma)  # Saída: 15
subtracao = 10 - 5
print(subtracao)  # Saída: 5
multiplicacao = 10 * 5
print(multiplicacao)  # Saída: 50
divisao = 10 / 5
print(divisao)  # Saída: 2.0
# Divisão inteira
divisao_inteira = 10 // 3
print(divisao_inteira)  # Saída: 3
# Resto da divisão
resto = 10 % 3
print(resto)  # Saída: 1
# Potenciação
potencia = 2 ** 3
print(potencia)  # Saída: 8
# Em resumo, os números em Python podem ser usados para realizar uma variedade de operações matemáticas, e a linguagem oferece suporte para diferentes tipos de números, incluindo inteiros, números de ponto flutuante e números complexos.
#exemplo:
print(10 + 5)  # Saída: 15
print(10 - 5)  # Saída: 5
print(10 * 5)  # Saída: 50
print(10 / 5)  # Saída: 2.0
print(10 // 3)  # Saída: 3
print(10 % 3)  # Saída: 1
print(2 ** 3)  # Saída: 8
#Numero nao usa aspas, pois são valores numéricos e não strings.
#Uso da , para string e . para numeros, por exemplo:
print("ola",5+3)  # Saída: ola 8
#A vírgula é usada para separar diferentes itens em uma função print(), enquanto o ponto é usado para indicar a parte decimal de um número de ponto flutuante. Por exemplo:
print("O resultado da divisão é:", 10 / 3)  # Saída: O resultado da divisão é: 3.3333333333333335
#Em resumo, a vírgula é usada para separar itens em uma função print(), enquanto o ponto é usado para indicar a parte decimal de um número de ponto flutuante.      
#variaveis em Python:
#Em Python, as variáveis são usadas para armazenar valores que podem ser usados posteriormente no código. Para criar uma variável, basta atribuir um valor a um nome de variável usando o operador de atribuição (=). Aqui estão alguns exemplos de como usar variáveis em Python:
# Criando variáveis -Toda variavel e um objeto, toda variavel recebe um tipo de dado, como string, inteiro, float, etc. Que seriam valores que a variavel pode receber.
nome = "Maria"
idade = 30
altura = 1.65
# Imprimindo variáveis
print(nome)  # Saída: Maria
print(idade)  # Saída: 30
print(altura)  # Saída: 1.65

#Outra forma de imprimir variáveis
print(nome, idade, altura)  # Saída: Maria 30 1.65
# Usando variáveis em operações
soma_idade = idade + 5
print(soma_idade)  # Saída: 35

#INPUT
#Em Python, a função input() é usada para obter entrada do usuário. Ela permite que o programa solicite ao usuário que digite algo e, em seguida, armazena essa entrada em uma variável para uso posterior. Aqui estão alguns exemplos de como usar a função input() em Python
# Solicitando entrada do usuário
nome = input("Digite seu nome: ") #Nome recebe o resultado de input qual e o seu nume, o input e uma função que recebe uma string como argumento, essa string e a mensagem que sera exibida para o usuario, e o resultado do input e armazenado na variavel nome.
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")

print(nome,idade,altura)
        

#input sginifica leitura, ou seja, o programa esta lendo a entrada do usuario, e armazenando essa entrada em uma variavel para uso posterior. O input sempre retorna uma string, mesmo que o usuario digite um numero, entao se quisermos usar a idade e altura como numeros, precisamos converter essas strings para o tipo de dado apropriado usando as funções int() ou float()
#print significa escrita, ou seja, o programa esta escrevendo uma mensagem para o usuario, e pode incluir variaveis para mostrar o resultado da entrada do usuario. 