from math import sin,cos,tan,radians

angulo=float(input("Digite o angulo que deseja calcular: "))
seno=sin(radians(angulo))
print("O seno de {} é igual á {:.2f}".format(angulo,seno))

cosseno=cos(radians(angulo))
print("O cosseno de {} é igual á {:.2f}" .format(angulo,cosseno))

tangente=tan(radians(angulo))
print("A tangente de {}é igual á {:.2f}".format(angulo,tangente))

#!outra forma
import math
angulo=float(input("Digite o angulo que deseja calcular: "))
seno=math.sin(math.radians(angulo))
print("O seno de {} é igual á {:.2f}".format(angulo,seno))

cosseno=math.cos(math.radians(angulo))
print("O cosseno de {} é igual á {:.2f}" .format(angulo,cosseno))

tangente=math.tan(math.radians(angulo))
print("A tangente de {}é igual á {:.2f}".format(angulo,tangente))





