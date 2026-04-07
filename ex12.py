n1 = float (input("Digite a primeira nota: "))
n2 = float (input("Digite a segunda nota: "))
m = (n1+n2) /2
print("A sua media foi: {:.1f}".format(m))
if m >= 5:
    print("Aprovado Sua media foi: {:.1f}".format(m))
else:
    print("Reprovado Sua media foi: {:.1f}".format(m) + " Estude mais para a proxima prova")
