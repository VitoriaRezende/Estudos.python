velocidade = float(input("Digite quantos km/h você está dirigindo: "))
if velocidade >= 80:
    print("Você foi multado por excesso de velocidade! Sua multa é de R$ 7,00 por cada km/h acima do limite.")
    multa = (velocidade - 80) * 7
    print("O valor da sua multa é: R$ {:.2f}".format(multa))
else:
    print("Parabéns, você está dirigindo dentro do limite de velocidade!")