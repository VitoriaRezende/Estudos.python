valor=float(input("Qual o valor do produto? R$"))
print("Escolha a forma de pagamento: \n1- À vista dinheiro/cheque \n2- À vista cartão \n3- 2x no cartão \n4- 3x ou mais no cartão")
opcao=int(input("Digite a opção desejada: "))
if opcao==1:
    desconto=valor*0.10
    print("Você recebeu um desconto de R$ {:.2f} e o valor final do produto é de R$ {:.2f}".format(desconto, valor-desconto))
elif opcao==2:
    desconto=valor*0.05
    print("Você recebeu um desconto de R$ {:.2f} e o valor final do produto é de R$ {:.2f}".format(desconto, valor-desconto))
elif opcao==3:
    print("O valor do produto será dividido em 2x de R$ {:.2f} sem juros".format(valor/2))
elif opcao==4:
    juros=valor*0.20
    print("O valor do produto será dividido em 3x ou mais de R${:.2f} com juros, o valor final do produto é de R$ {:.2f}".format((valor+juros)/3, valor+juros)) #formatação para mostrar o valor da parcela e o valor final do produto com juros
else:
    print("Opção inválida, tente novamente")