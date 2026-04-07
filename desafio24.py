cidade=input("Digite o nome da cidade onde você nasceu: ").strip() #strip() remove os espaços em branco no início e no final da string
print(cidade[:6].upper() == "SAO PAULO") #verifica se os primeiros 6 caracteres da string são iguais a "SAO PAULO" (ignora maiúsculas e minúsculas) e imprime o resultado (True ou False) true se for igual e false se for diferente
    