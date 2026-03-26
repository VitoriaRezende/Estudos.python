from math import sqrt, ceil, radians, cos, sin, tan, log, exp, trunc

cat=float(input("Digite o comprimento do cateto oposto: "))
adj=float(input("Digite o comprimento do cateto adjacente:  "))
hip=sqrt(cat**2 + adj**2)
print("A hipotenusa é igual a {}".format(int(hip)))

#!-------------------------------------------------
import math
cat=float(input("Digite o comprimento do cateto oposto: "))
adj=float(input("Digite o comprimento do cateto adjacente:  "))
hi=math.hypot(cat, adj)
print("A hipotenusa é igual a {:.2f}".format(hi))
#!-------------------------------------------------
from math import hypot as hipotenusa
cat=float(input("Digite o comprimento do cateto oposto: "))
adj=float(input("Digite o comprimento do cateto adjacente:  "))
hi=hipotenusa(cat, adj)
print("A hipotenusa é igual a {:.2f}".format(hi))
#!-------------------------------------------------
from math import hypot
cat=float(input("Digite o comprimento do cateto oposto: "))
adj=float(input("Digite o comprimento do cateto adjacente:  "))
hi=hypot(cat, adj)
print("A hipotenusa é igual a {:.2f}".format(hi))
#!-------------------------------------------------
