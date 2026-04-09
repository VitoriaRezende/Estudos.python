sexo=input("Digite o sexo (M/F): ").upper() #upper() converte a string para maiúscula, garantindo que a comparação seja feita de forma consistente, independentemente de o usuário digitar "m", "M", "f" ou "F". O programa então verifica o valor da variável "sexo" e imprime uma mensagem indicando se o sexo é masculino, feminino ou inválido.
ano=int(input("Digite o ano de nascimento: "))
if sexo=="F":
    print("Voce é do sexo feminino logo não precisa se alistar ao serviço militar")
elif sexo=="M":
  idade=2026-ano
  if idade<18:
    print("Voce tem {} anos, ainda faltam {} anos para o alistamento".format(idade,18-idade))
  elif idade==18:
    print("Voce tem {} anos, é hora de se alistar".format(idade))
  elif idade>18:
    print("Voce tem {} anos, voce deveria ter se alistado a {} anos, infelizmente ja passou do prazo".format(idade,idade-18))
else:
    print("Sexo invalido, tente novamente")
   