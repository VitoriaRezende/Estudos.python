km = int(input("Digite a distancia em km: "))
if km <= 200:
    preco = km * 0.50
else:
    print("Oba, o km digitado {} é maior que 200km".format(km))
    preco = km * 0.45
    print("O valor da sua passagem é: R$ {:.2f}".format(preco))