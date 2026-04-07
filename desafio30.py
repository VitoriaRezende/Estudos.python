numero = int(input("Digite um numero:   "))
if numero % 2 == 0 : # % significa o resto da divisao, entao se o numero for divisivel por 2 e o resto for igual a 0, o numero é par
    print("O numero {} é par".format(numero))
else:
    print("O numero {} é impar".format(numero))