salario=float(input("Digite o salario do funcionario: "))
#O programa solicita ao usuário que insira o salário do funcionário e armazena esse valor na variável "salario" como um número de ponto flutuante (float). O programa então verifica o valor do salário e aplica um aumento de acordo com as seguintes condições: se o salário for menor ou igual a 280, o aumento será de 20%; se o salário for maior que 280 e menor ou igual a 700, o aumento será de 15%; se o salário for maior que 700 e menor ou igual a 1500, o aumento será de 10%; e se o salário for maior que 1500, o aumento será de 5%. O programa calcula o valor do aumento, o novo salário e imprime os resultados formatados na tela.
if salario >= 1250:
    aumento= salario *0.10
else: 
    aumento=salario*0.15
    print("O salario antes do aumento era de R${:.2f} e agora após o aumento passou a ser R${:.2F}".format(salario,salario+aumento))