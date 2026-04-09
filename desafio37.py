numero=int(input("Digite um numero inteiro:"))
escolha=int(input("Escolha uma das bases para conversão: \n1- Binário \n2- Octal \n3- Hexadecimal\n"))
if escolha==1:
    print("O numero {} convertido para binário é igual a {}".format(numero,bin(numero)[2:]))
elif escolha==2:
    print("O numero {} convertido para octal é igual a {}".format(numero,oct(numero)[2:]))
elif escolha==3:
    print("O numero {} convertido para hexadecimal é igual a {}".format(numero,hex(numero)[2:]))
else:
    print("Opção invalida, tente novamente")