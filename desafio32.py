from datetime import date #Importa a classe "date" do módulo "datetime" para obter a data atual.
ano = int(input("Qual ano você deseja verificar se é bissexto? Coloque 0 para o ano atual: "))#O programa solicita ao usuário que insira um ano e armazena esse valor na variável "ano" como um número inteiro.
if ano == 0:#Se o usuário inserir 0, o programa atribui o ano atual à variável "ano" usando a função "date.today().year", que retorna o ano atual.
    ano = date.today().year #A função "date.today()" retorna a data atual, e o atributo ".year" extrai apenas o ano dessa data. Assim, se o usuário escolher verificar o ano atual, o programa usará automaticamente o ano em que está sendo executado para determinar se é bissexto ou não.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:#Ano precida ser divisivel por quatreo e também nao pode ser divisivel por 100 seu resutado tem que ser diferente de zero ou ano precisa ser divisivel por 400 com o resultado igual a zero para ser considerado bissexto
    ##A condição verifica se o ano é divisível por 4 e, ao mesmo tempo, não é divisível por 100, ou seja, é um ano bissexto. Se ambas as condições forem verdadeiras, o programa imprime que o ano é bissexto; caso contrário, imprime que o ano não é bissexto.
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))


#and significa "e" e é usado para combinar duas ou mais condições. No exemplo acima, a condição verifica se o ano é divisível por 4 e, ao mesmo tempo, não é divisível por 100, ou seja, é um ano bissexto. Se ambas as condições forem verdadeiras, o programa imprime que o ano é bissexto; caso contrário, imprime que o ano não é bissexto.
#or significa "ou" e é usado para combinar duas ou mais condições, onde pelo menos uma delas deve ser verdadeira para que a condição geral seja considerada verdadeira. No exemplo acima, a condição verifica se o ano é divisível por 4 e, ao mesmo tempo, não é divisível por 100, ou seja, é um ano bissexto. Se pelo menos uma das condições for verdadeira, o programa imprime que o ano é bissexto; caso contrário, imprime que o ano não é bissexto.
#not significa "não" e é usado para negar uma condição. No exemplo acima, a condição verifica se o ano é divisível por 4 e, ao mesmo tempo, não é divis