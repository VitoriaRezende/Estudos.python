#!Tipos primitivos em Python
#!Em Python, existem vários tipos primitivos de dados que são usados para armazenar diferentes tipos de informações. Aqui estão alguns dos tipos primitivos mais comuns em Python:
#!1. Números (int, float, complex, bool) - Os números em Python podem ser inteiros (int), números de ponto flutuante (float), números complexos (complex) e booleanos (bool). Os inteiros são usados para representar números inteiros, os números de ponto flutuante são usados para representar números decimais, os números complexos são usados para representar números com parte real e imaginária, e os booleanos são usados para representar valores verdadeiros ou falsos.
#*2. Strings (str) som usadas para representar texto. Elas são criadas usando aspas simples (' ') ou aspas duplas (" "). Por exemplo:
#*3. Booleanos (bool) so aceitam os valores True ou False, e são usados para representar condições ou estados de verdade. 
#*4. None (NoneType) so usado para representar a ausência de valor ou a falta de um valor. Ele é frequentemente usado para indicar que uma variável não tem um valor atribuído ou que uma função não retorna um valor.
#*5. Listas (list) sao usadas para armazenar uma coleção de itens ordenados e mutáveis. Elas são criadas usando colchetes [] e os itens são separados por vírgulas. Por exemplo:
minha_lista = [1, 2, 3, "quatro", True]
print(minha_lista)  # Saída: [1, 2, 3,"quatro", True]

#*6. Tuplas (tuple) sao usadas para armazenar uma coleção de itens ordenados e imutáveis. Elas são criadas usando parênteses () e os itens são separados por vírgulas. Por exemplo:
minha_tupla = (1, 2, 3, "quatro", True)
print(minha_tupla)  # Saída: (1, 2, 3, "quatro", True)

#*7. Dicionários (dict) sao usados para armazenar uma coleção de pares chave-valor. Eles são criados usando chaves {} e os pares chave-valor são separados por vírgulas. Por exemplo:
meu_dicionario = {"nome": "Maria", "idade": 30, "altura": 1.65}
print(meu_dicionario)  # Saída: {'nome': 'Maria', 'idade': 30, 'altura': 1.65}

#*8. Conjuntos (set) sao usados para armazenar uma coleção de itens únicos e não ordenados. Eles são criados usando chaves {} ou a função set(). Por exemplo:
meu_conjunto = {1, 2, 3, "quatro", True}
print(meu_conjunto)  # Saída: {1, 2, 3, "quatro", True}

#*9. Bytes (bytes) sao usados para representar dados binários imutáveis. Eles são criados usando a função bytes() ou prefixando uma string com b. Por exemplo:
meus_bytes = b"Hello, world!"
print(meus_bytes)  # Saída: b'Hello, world!'    


#*10. Bytearrays (bytearray) sao usados para representar dados binários mutáveis. Eles são criados usando a função bytearray() ou prefixando uma string com b. Por exemplo:
meu_bytearray = bytearray(b"Hello, world!")
print(meu_bytearray)  # Saída: bytearray(b'Hello, world!')


#*11. Memóriaview (memoryview)sao usados para acessar os dados de um objeto de bytes sem copiá-los. Eles são criados usando a função memoryview() e podem ser usados para manipular os dados de um objeto de bytes de forma eficiente. Por exemplo:
meu_bytes = b"Hello, world!"
meu_memoryview = memoryview(meu_bytes)
print(meu_memoryview[0])  # Saída: 72 (o valor ASCII da letra 'H')

#*12. Range (range) sao usados para representar uma sequência de números inteiros. Eles são criados usando a função range() e podem ser usados em loops para iterar sobre uma sequência de números. Por exemplo:
meu_range = range(1, 10)
print(meu_range)  # Saída: range(1, 10)
for i in meu_range:
    print(i)  # Saída: 1, 2, 3, 4, 5, 6, 7, 8, 9
    
#*13. Frozenset (frozenset) sao usados para armazenar uma coleção de itens únicos e imutáveis. Eles são criados usando a função frozenset() e são semelhantes aos conjuntos, mas não podem ser modificados após a criação. Por exemplo:
meu_frozenset = frozenset([1, 2, 3, "quatro", True])
print(meu_frozenset)  # Saída: frozenset({1, 2, 3, "quatro", True})

#*14. Tipo de dados personalizado (classes)sao usados para criar tipos de dados personalizados usando classes. Eles permitem que você defina seus próprios tipos de dados com atributos e métodos personalizados. Por exemplo:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade  
pessoa1 = Pessoa("Maria", 30)
print(pessoa1.nome)  # Saída: Maria
print(pessoa1.idade)  # Saída: 30

#!Cada tipo de dado tem suas próprias características e usos específicos. Por exemplo, os números são

#?-------------------------------------
#*Numeros inteiros (int) são usados para representar números inteiros, como 1, 2, 3, etc. Eles podem ser positivos ou negativos e não possuem parte decimal. Por exemplo:
n1=int(input("Digite um número: "))
n2=int(input("Digite outro número: "))
soma = n1 + n2
print("A soma dos números é:", soma)
#?-------------------------------------
n1=float(input("Digite um número: "))
n2=float(input("Digite outro número: "))
soma = n1 + n2
print("A soma dos números é:", soma)
#?-------------------------------------
#Forma de representar print usando a função format()
n1=float(input("Digite um número: "))
n2=float(input("Digite outro número: "))
soma = n1 + n2
print("A soma dos números é: {}".format(soma))

#?-------------------------------------

n1= int(input("Digite um número: "))
print(type(n1))  # Saída: <class 'int'> quweo dizer que a variável n1 é do tipo inteiro (int). e estou mostrando o tipo da variável usando a função type().

#?-------------------------------------
n1=int(input("Digite um número: "))
n2=int(input("Digite outro número: "))
soma = n1 + n2
print("A soma entre ",n1, "e", n2, "é igual a", soma)  # Saída: A soma entre 5 e 10 é igual a 15
#?-------------------------------------
n1-=int(input("Digite um número: "))
n2=int(input("Digite outro número: "))
soma = n1 + n2
print("A soma entre {}, e {}, é igual a {}".format(n1, n2, soma))  # Saída: A soma entre 5 e 10 é igual a 15
#?-------------------------------------
n=str(input("Digite um número: "))
print(type(n))  #! Saída: <class 'str'> que significa que a variável "n" é do tipo string (str).
#!Aqui podemos usar para converter a string em um número inteiro usando a função int(), ou em um número de ponto flutuante usando a função float(). Por exemplo:
#!so retiramos o type() para mostrar o tipo da variável, e usamos a função int() para converter a string em um número inteiro, ou a função float() para converter a string em um número de ponto flutuante. Por exemplo:

n=int(input("Digite um número: "))
print(n) # Saída: <class 'int'> que significa que a variável n é do tipo inteiro (int).
#?-------------------------------------
n=bool(input("Digite um número: "))
print(n)  # Saída: True ou False, dependendo do valor digitado pelo usuário se o usuario nao digitar nada, ou digitar 0, ou digitar False, a saída será False. Caso contrário, a saída será True.
#?-------------------------------------
#variavel isnumeric() é um método de string em Python que verifica se todos os caracteres em uma string são numéricos. Ele retorna True se todos os caracteres forem numéricos e False caso contrário. Por exemplo:
n=input("Digite um número: ")
if n.isnumeric(): #Se sim ele retorna True, caso contrário, retorna False. Por exemplo:
    print("A string é numérica.")
else:    print("A string não é numérica.")

#!Ou
n=input("Digite um número: ") 
print(n.isnumeric()) #* Saída: True ou False, dependendo do valor digitado pelo usuário se o usuario digitar apenas números, a saída será True. Caso contrário, a saída será False.
#?-------------------------------------
#!isalpha() é um método de string em Python que verifica se todos os caracteres em uma string são alfanuméricos (ou seja, letras ou números). Ele retorna True se todos os caracteres forem alfanuméricos e False caso contrário. Por exemplo:
n=input("Digite um número: ")
if n.isalpha(): #Se sim ele retorna True, caso contrário, retorna False. Por exemplo:
    print("A string é alfanumérica.")
else:    print("A string não é alfanumérica.")  
 #!Ou
n=input("Digite um número: ") 
print(n.isalpha())  #* Saída: True ou False, dependendo do valor digitado pelo usuário se o usuario digitar apenas letras, a saída será True. Caso contrário, a saída será False.
#?-------------------------------------
