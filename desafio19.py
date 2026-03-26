aluno1=input("Digite o nome do primeiro aluno: ")
aluno2=input("Digite o nome do segundo aluno: ")
aluno3=input("Digite o nome do terceiro aluno: ")
aluno4=input("Digite o nome do quarto aluno: ")

from random import choice 

lista=(aluno1, aluno2, aluno3, aluno4)    
escolhido=choice(lista)
print("Ó aluno escolhido foi {}" .format(escolhido))

