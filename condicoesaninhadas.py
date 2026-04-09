#Condiçoes Aninhadas
#Condiçoes aninhadas são estruturas de controle de fluxo em que uma condição é colocada dentro de outra condição. 
# Isso permite que você crie decisões mais complexas e específicas em seu código. 
# Por exemplo, você pode ter uma condição principal que verifica se um número é positivo, e dentro dessa condição,
# outra condição que verifica se o número é par ou ímpar.
#Exemplo de código com condições aninhadas usando if-else e elif:
#or significa ou
#and significa e
#not significa não
#IN significa em uma lista ou conjunto de valores EXEMPLO: if nome in ["Alice", "Vitoria", "Maria"]: SIGNIFICA QUE SE O NOME DO USUÁRIO FOR IGUAL A QUALQUER UM DOS NOMES NA LISTA, A CONDIÇÃO SERÁ VERDADEIRA.


nome=input("Digite seu nome: ")
if nome == "Alice":
    print("Nossa que nome lindo!") #Condição simples para verificar se o nome é "Alice" e imprimir uma mensagem.
elif nome == "Vitoria" or nome == "Maria" or nome == "João": #Condição composta para os nomes "Vitoria", "Maria" e "João", usando o operador lógico "or" para verificar se o nome do usuário corresponde a qualquer um desses nomes.
    print("Seu nome é bem bonito, {}!".format(nome)) #Condição composta para os nomes "Vitoria" e "Maria", usando a função format para incluir o nome do usuário na mensagem.
elif nome in ("Jessica Ana"):
    print("Seu nome é bem bonito, {}!".format(nome)) #Condição composta para os nomes "Jessica" e "Ana", usando a função format para incluir o nome do usuário na mensagem.
else:
    print("Seu nome é bem normal, {}!".format(nome)) #Condição composta para outros nomes, usando a função format para incluir o nome do usuário na mensagem.

print("Olá, {}!".format(nome))
