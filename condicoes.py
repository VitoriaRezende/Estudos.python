#CONDIÇÃOES
#condições são estruturas de controle que permitem executar um bloco de código apenas se uma determinada condição for verdadeira. As condições são usadas para tomar decisões no código, como por exemplo, verificar se um número é maior que outro, se uma string contém uma determinada palavra, etc. As condições são escritas usando os operadores de comparação, como ==, !=, >, <, >=, <=, e os operadores lógicos, como and, or, not. As condições são usadas em estruturas de controle como if, elif e else para executar diferentes blocos de código dependendo do resultado da condição.
#Se acontecer uma coisa faça isso, se acontecer outra coisa faça aquilo, se não acontecer nada faça outra coisa.
#Se e representado por if, 
#senao se e representado por elif,
#senao e representado por else.
#diferenca entre elif e else: elif é usado para verificar uma condição adicional se a condição anterior for falsa, enquanto else é usado para executar um bloco de código se todas as condições anteriores forem falsas. Por exemplo:
x = 10
if x > 10:
    print("x é maior que 10")
elif x == 10:
    print("x é igual a 10")
else:
    print("x é menor que 10") #Nesse exemplo, o bloco de código dentro do if será executado se x for maior que 10, 
                              #o bloco de código dentro do elif será executado se x for igual a 10, e o bloco de código dentro do else será executado
                              # se x for menor que 10. Se x for igual a 10, o resultado será "x é igual a 10", e o bloco de código dentro do else não será executado. 
                              # Se x fosse menor que 10, o resultado seria "x é menor que 10", e o bloco de código dentro do elif não seria executado.
    
#TIPOS DE CONDIÇÕES
#1. Condição Simples: É uma condição que verifica apenas uma expressão. Por exemplo if x > 10: print("x é maior que 10")
#2. Condição Composta: É uma condição que verifica mais de uma expressão usando os operadores lógicos and, or, not. Por exemplo if x > 10 and y < 5: print("x é maior que 10 e y é menor que 5")
#3. Condição Aninhada: É uma condição que contém outra condição dentro dela. Por exemplo if x > 10: if y < 5: print("x é maior que 10 e y é menor que 5")
#4. Condição Encadeada: É uma condição que verifica várias expressões usando os operadores lógicos and, or, not. Por exemplo if x > 10 and y < 5 or z == 0: print("x é maior que 10 e y é menor que 5 ou z é igual a 0")

#EXEMPLO DE CONDIÇÃO SIMPLES
x = 15
if x > 10:
    print("x é maior que 10")
#EXEMPLO DE CONDIÇÃO COMPOSTA
x = 15
y = 3
if x > 10 and y < 5:
    print("x é maior que 10 e y é menor que 5")
#EXEMPLO DE CONDIÇÃO ANINHADA
x = 15
y = 3
if x > 10:
    if y < 5:
        print("x é maior que 10 e y é menor que 5")
        
#EXEMPLO DE CONDIÇÃO ENCADEADA
x = 15
y = 3
z = 0
if x > 10 and y < 5 or z == 0:
    print("x é maior que 10 e y é menor que 5 ou z é igual a 0")
    

#!----------------------------------------------------------------
carro=input("O carro esta virando a esquerda? (s/n) ")
if carro == "s":
    print("Vire a esquerda")
else:
    print("Siga em frente")
    
#Nessa condição ou ele retorna a true verdadeiro ou ele retorna a false falso,
# sempre sera uma das duas opções, nunca vai ser as duas opções ao mesmo tempo,
# ou seja, ou ele vira a esquerda ou ele segue em frente, nunca vai ser as duas coisas ao mesmo tempo.
#AND AS DUAS AFIRMACOES PRECISAM SER  VERDADEIRA
#OR UM OU OUTRO PRECIDA SER VERDADEIRO
#NOT EU NEGO A AFIRMAÇÃO


#!----------------------------------------------------------------

tempo=int(input("Qual o ano do seu carro?")) #Se carro for menor ou igual a 5 logo sera carro novo se nao for sera imprimido carro velho
if tempo <= 5:
    print("Carro novo")
else:
    print("Carro velho")
    print("Fim do programa")
#!----------------------------------------------------------------

    