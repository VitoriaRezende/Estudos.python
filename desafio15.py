dias = int(input("Quantos dias voce alugou o carro?   "))
km = float (input ("Quantos km voce rodou?  "))
preco = (dias*60) + (km*0.15)
print("O valor do aluguel do carro é {}" .format(preco))