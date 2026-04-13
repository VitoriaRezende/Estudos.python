#? Entrada de dados  - Programa esta recebendo (colhendo) dados do usuario
nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
peso=float(input("Digite seu peso em kg: "))
altura=float(input("Digite sua altura em metros: "))

#? Processamento de dados
imc=peso/(altura**2) 
#!Com os dados recebidos do usuario o programa começa a fazer o que eu pedi/ solicitei, nesse caso o programa calcula o imc
#!usando a fórmula peso dividido pela altura ao quadrado. O resultado do cálculo é armazenado na variável "imc". 
# !O programa então pode usar esse valor para fornecer informações sobre a saúde do usuário com base no índice de massa corporal (IMC).


#? Saída de dados
print("Olá {}, com base nos seus dados. Seu IMC é de {:.1f}".format(nome, imc))
#! A saida de dados e o final, aonde apos colher os dados, fazer o processamento que coloquei para o programa, 
#!entao a saida seria o resultado