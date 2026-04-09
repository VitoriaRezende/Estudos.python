a=float(input("Digite o primeiro lado do triangulo: "))
b=float(input("Digite o segundo lado do triangulo: "))
c=float(input("Digite o terceiro lado do triangulo: "))

if a + b > c and a + c > b and b + c > a:
    
 if a == b == c:
         print("Triângulo equilátero")
elif a==b==c:
    print("Os lados formam um triangulo equilatero")
elif a==b or a==c or b==c:
    print("Os lados formam um triangulo isosceles")
elif a!=b and a!=c and b!=c:
    print("Os lados formam um triangulo escaleno")
else:
    print("Os lados não formam um triangulo")
