#? BIBLIOTECA MATH  - Significa "matemática" e fornece funções matemáticas como raiz quadrada, seno, cosseno, etc.
#! ceil - Arredonda um número para cima
#! floor - Arredonda um número para baixo
#! sqrt - Calcula a raiz quadrada de um número
#! sin - Calcula o seno de um ângulo (em radianos)
#! cos - Calcula o cosseno de um ângulo (em radianos)
#! tan - Calcula a tangente de um ângulo (em radianos)
#! log - Calcula o logaritmo natural de um número
#! exp - Calcula a exponenciação de um número
#!random - Fornece funções para gerar números aleatórios, como randint, random, choice, etc.
#!trunc - Trunca um número, ou seja, remove a parte decimal e retorna apenas a parte inteira
#!pow - Calcula a potência de um número, ou seja, eleva um número a uma determinada potência
#!factorial - Calcula o fatorial de um número, ou seja,o produto de todos os números inteiros positivos menores ou iguais a um determinado número

#!from math import sqrt, sin, cos, tan, log, exp quando quero usar apenas algumas funções do modulo math, para evitar ter que usar math.sqrt, math.sin, etc. toda vez que quiser usar uma função do modulo math. Dessa forma, posso usar sqrt, sin, cos, tan, log, exp diretamente no meu código, sem precisar usar o nome do modulo. Por exemplo:
from math import sqrt, sin, cos, tan, log, exp, radians
num = 16
raiz = sqrt(num)
print("A raiz quadrada de {} é {}".format(num, raiz))
angulo = 30
seno = sin(radians(angulo))
print("O seno de {} graus é {}".format(angulo, seno))
#?-------------------------------------------------

#exemplo de uso do modulo math:
import math
num = 16
raiz = math.sqrt(num)
print("A raiz quadrada de {} é {}".format(num, raiz))
#mais exemplos de uso do modulo math:
angulo = 30
seno = math.sin(math.radians(angulo)) #! A função math.radians converte o ângulo de graus para radianos, pois as funções trigonométricas do módulo math esperam os ângulos em radianos. O resultado do seno de 30 graus é 0.5, que é o valor correto. Se você não usar a função math.radians, o resultado será diferente, pois o seno de 30 radianos é um valor diferente do seno de 30 graus.
#!radiants - Converte um ângulo de graus para radianos
#!degrees - Converte um ângulo de radianos para graus
print("O seno de {} graus é {}".format(angulo, seno))


#? BIBLIOTECA OS - Fornece funções para interagir com o sistema operacional, como listar arquivos, criar pastas, etc.
#? BIBLIOTECA SYS - Fornece funções para interagir com o interpretador Python, como exibir argumentos de linha de comando, versão do Python, etc.
#? BIBLIOTECA TIME - Fornece funções para trabalhar com tempo, como exibir o tempo atual, pausar a execução do programa, etc.
#? BIBLIOTECA DATETIME - Fornece funções para trabalhar com datas e horas, como exibir a data e hora atual, apenas a data, apenas a hora, etc.  
#!-------------------------------------------------

#PRATICA
import math
num=int(input("Digite um numero: "))
raiz=math.sqrt(num)
print("A raiz quadrada do numero {} é {}".format(num,math.ceil(raiz))) #Exemplo de uso da função math.ceil para arredondar a raiz quadrada para cima
#!-------------------------------------------------
#usando from math import sqrt, ceil para evitar usar math.sqrt e math.ceil toda vez que quiser usar essas funções do módulo math. Dessa forma, posso usar sqrt e ceil diretamente no meu código, sem precisar usar o nome do módulo. Por exemplo:
from math import sqrt, ceil
num=int(input("Digite um numero: "))
raiz=sqrt(num)
print("A raiz quadrada do numero {} é {}". format(num,ceil(raiz)))
#!-------------------------------------------------

#from math import sqrt as raizquadrada exemplo

from math import sqrt as raizquadrada
num=int(input("Digite um numero: "))
raiz=raizquadrada(num)
print("A raiz quadrada do numero {} é {}". format(num,ceil(raiz)))
#apelidando a função sqrt como raizquadrada para facilitar o uso no código. Dessa forma, posso usar raizquadrada diretamente no meu código, sem precisar usar o nome do módulo ou a função original. Por exemplo:
#!-------------------------------------------------

#mostrar a parte inteira de um numero usando a função math.trunc
