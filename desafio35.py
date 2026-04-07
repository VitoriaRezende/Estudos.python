a=float(input("Digite o primeiro lado do triangulo: "))
b=float(input("Digite o segundo lado do triangulo: "))
c=float(input("Digite o terceiro lado do triangulo: "))
#O programa solicita ao usuário que insira os comprimentos dos três lados de um triângulo e armazena esses valores nas variáveis "a", "b" e "c" como números de ponto flutuante (float). O programa então verifica se os lados fornecidos podem formar um triângulo usando a condição de existência do triângulo, que afirma que a soma de dois lados deve ser maior que o terceiro lado para todos os pares de lados. Se a condição for satisfeita, o programa imprime que os lados formam um triângulo; caso contrário, imprime que os lados não formam um triângulo.
if a+b>c and a+c>b and b+c>a:
    print("Os lados formam um triangulo")
else:
    print("Os lados não formam um triangulo")
