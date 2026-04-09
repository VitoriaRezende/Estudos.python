peso=float(input("Digite seu peso em kg: "))
altura=float(input("Digite sua altura em metros: "))
altura=altura/100 #Convertendo a altura de metros para centímetros, dividindo o valor da altura por 100.
imc=peso/(altura**2) #

if imc<18.5:
    print("Seu IMC é de {:.1f} e você está abaixo do peso ideal".format(imc))
elif imc>=18.5 and imc<25:
    print("Seu IMC é de {:.1f} e você está com o peso ideal".format(imc))
elif imc>=25 and imc<30:
    print("Seu IMC é de {:.1f} e você está com sobrepeso".format(imc))
elif imc>=30 and imc<=40:
    print("Seu IMC é de {:.1f} e você está com obesidade".format(imc))
else:
    print("Seu IMC é de {:.1f} e você está com obesidade mórbida".format(imc))