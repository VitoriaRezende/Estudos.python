valor1=int(input("Digite o primeiro valor: "))
valor2=int(input("Digite o segundo valor:"))
valor3=int(input("Digite o terceiro valor: "))
#Valores são solicitados ao usuário e armazenados nas variáveis "valor1", "valor2" e "valor3" como números inteiros. verificando qual é o menor e o maior valor entre os três números fornecidos pelo usuário. O programa compara os valores usando estruturas condicionais (if) para determinar qual é o menor e qual é o maior, e depois imprime os resultados formatados na tela.
if valor1<valor2 and valor1<valor3:
    menor=valor1
if valor2<valor3 and valor2<valor1:
        menor=valor2
if valor3<valor1 and valor3<valor2:
    menor=valor3
if valor1>valor2 and valor1>valor3:
    maior=valor1
if valor2>valor3 and valor2>valor1:
    maior=valor2
if valor3>valor1 and valor3>valor2:
    maior=valor3
    print("O menor valor é {} e o maior valor é {}".format(menor,maior))