print("VAMOS JOGAR JOKENPÔ!")
from random import choice #Importa a função "choice" do módulo "random", que é usada para fazer escolhas aleatórias.
itens=("Pedra", "Papel", "Tesoura")
computador=choice(itens) #A variável "computador" recebe uma escolha aleatória da tupla "itens", que contém as opções do jogo: "Pedra", "Papel" e "Tesoura". Isso simula a jogada do computador.
print("Escolha uma opção: \n[0] Pedra \n[1] Papel \n[2] Tesoura")
jogador=int(input("Digite a sua jogada: "))
print("O computador jogou {}".format(computador))
if jogador==0: #Se o jogador escolher "Pedra" (0), o programa
    if computador=="Pedra":
        print("Empate!")
    elif computador =="Papel":
        print("Computador venceu!")
    elif computador=="Tesoura":
        print("Jogador venceu!")
    elif jogador ==1:
        if computador=="Pedra":
            print("Jogador Venceu")
    elif computador =="Papel":
        print("Empate!")
    elif computador=="Tesoura":
        print("Computador venceu!")
    elif jogador ==2:
        if computador == "Pedra":
            print("Computador Venceu!")
        elif computador == "Papel":
            print("Jogador Venceu!")
        elif computador == "Tesoura":
            print("Empate!")
else:
    print("Jogada inválida, tente novamente!")
            