#Operaçoes aritmeticas
soma = 10 + 5 #Soma é a operação de adicionar dois números. O resultado é a soma dos números. Por exemplo, 10 + 5 é igual a 15.
subtracao = 10 - 5 #Subtração é a operação de subtrair um número de outro. O resultado é a diferença entre os números. Por exemplo, 10 - 5 é igual a 5.
multiplicacao = 10 * 5 #Multiplicação é a operação de multiplicar dois números. O resultado é o produto dos números. Por exemplo, 10 * 5 é igual a 50.
divisao = 10 / 5 #Divisão sempre retorna um número float, mesmo que o resultado seja um número inteiro. Se quiser uma divisão inteira, use o operador //.
divisao_inteira = 10 // 3 #Divisão inteira
exponenciacao = 10 ** 5 #10 elevado a 5
modulo = 10 % 3  #Resto da divisão de 10 por 3
raiz_quadrada = 10 ** 0.5 #Raiz quadrada de 10
raiz_cubica = 10 ** (1/3) #Raiz cúbica de 10
potencia=pow(10, 5) #Outra forma de calcular a potência, onde o primeiro argumento é a base e o segundo é o expoente. O resultado é o mesmo que 10 ** 5, ou seja, 100000.
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Divisão Inteira:", divisao_inteira)
print("Exponenciação:", exponenciacao)
print("Módulo:", modulo)
print("Raiz Quadrada:", raiz_quadrada)
print("Raiz Cúbica:", raiz_cubica)
print("Potência:", potencia)

#Ordem de De Prioridade
#1. Parênteses ()
#2. Exponenciação **
#3. Multiplicação * e Divisão / (da esquerda para a direita)
#4. Adição + e Subtração - (da esquerda para a direita)
resultado = 10 + 5 * 2 #A multiplicação é realizada antes da adição, então o resultado é 10 + (5 * 2) = 10 + 10 = 20
print("Resultado:", resultado)



