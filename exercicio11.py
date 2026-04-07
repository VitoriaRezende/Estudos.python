nome = input("Qual o seu nome? ") #Entrada de dados para o nome do usuario
if nome == "Vitoria": #Condicao para verificar se o nome do usuario é igual a "Vitoria"
    print("Olá, Vitoria! Que nome bonito!") #Se a condicao for verdadeira, imprime "Olá, Vitoria!"
else: #Se a condicao for falsa, executa o bloco de codigo abaixo    
    print("seu nome é tao normal") #Imprime "Olá, " seguido do nome do usuario e um ponto de exclamação
    print("Bom dia, {}!".format(nome))
    