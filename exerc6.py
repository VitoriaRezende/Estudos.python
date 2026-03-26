#nome = input("Digite seu nome: ")
#print("Prazer em te conhecer {}!".format(nome))

#n1=int(input("Digite um numero: "))
#n2=int(input("Digite outro numero:"))
#print("A soma vale {}".format(n1+n2))
#Uso como variavel se ainda vou fazer uso  caso não posso somente somar 

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero:"))
soma = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print( """A soma Vale {},
      A multiplicação vale {},
      A divisão vale {:.3f}, #serve para limitar o numero de casas decimais
      A divisão inteira vale {},
      A exponenciação vale {}"""
      .format(soma,m,d,di,e)
      ) 
#uso end para evitar a quebra de linha
#!print("A soma vale {},".format(soma), end=" ")
#!print("A multiplicação vale {},".format(m), end=" ")
#!print("A divisão vale {:.3f},".format(d), end=" ")
#!print("A divisão inteira vale {},".format(di), end=" ")
#!print("A exponenciação vale {}.".format(e))

    