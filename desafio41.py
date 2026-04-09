ano=int(input("Digite o ano de nascimento: "))
idade=2026-ano
if idade<=9:
    print("Sua idade é {} anos, categoria: MIRIM".format(idade))
elif idade>9 and idade<=14:
    print("Sua idade é {} anos, categoria: INFANTIL".format(idade))
elif idade >14 and idade <=19:
    print("Sua idade é {} anos, categoria: JUNIOR".format(idade))
elif idade <=20:
    print("Sua idade é {}anos, categoria : senior ".format(idade))
else:
    print("Sua idade é {} anos, categoria: MASTER".format(idade))