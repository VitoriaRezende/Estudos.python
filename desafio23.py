#Desafio 23 - Separando dígitos de um número
#numero=int(input("Digite um número: "))
#n=str(numero)
# print("Analisando o numero {}" .format(numero))
#print("unidade {}".format(n[3]))
#print("Dezena {}".format(n[2]))
#print("Centena : {}".format(n[1]))
#print("Milhar : {}".format(n[0]))\\
    
num=int(input("Digite um número: "))
u=num//1%10 #pega o número e divide por 1 para pegar a unidade, depois pega o resto da divisão por 10 para pegar o último dígito
d = num//10%10 #pega o número e divide por 10 para pegar a dezena, depois pega o resto da divisão por 10 para pegar o último dígito
c=num//100%10 #pega o número e divide por 100 para pegar a centena, depois pega o resto da divisão por 10 para pegar o último dígito
m=num//1000%10 #pega o numero e divide por 1000 para pegar a milhar e depois pega o resto da divisao por 10 para pegar o último dígito porque o resto da divisao por 10 sempre vai pegar o último dígito do número resultante da divisão inteira
print("Analisando o numero{} ".format(num))
print("Unidade : {}".format(u))
print("Dezena : {}".format(d))
print("Centena : {}".format(c))
print("Milhar : {}".format(m))
