#Exercicio de emprestimo
valor=float(input("Digite o valor da casa que deseja comprar: "))
salario=float(input("Digite o seu salario: "))
anos=int(input("Digite em quantos anos deseja pagar: "))
prestacao=valor/(anos*12)
if prestacao>salario*0.30:
    print("Ops, infelizmente seu emprestimo foi negado, valor da parcela é maior que 30% do seu salario")
else:
    print("Parabens, seu emprestimo foi aprovado, o valor da parcela é de R${:.2f}".format(prestacao))