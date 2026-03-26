from random import shuffle

fruta1=input("digite o nome da primeira fruta: ")
fruta2=input("digite o nome da segunda fruta: ")
fruta3=input("digite o nome da terceira fruta: ")

lista = [fruta1, fruta2, fruta3] 

shuffle(lista)

print("A ordem de apresentação da fruta será")
print(lista)
#!------------------------------------
import random
 
fruta1=input("digite o nome da primeira fruta: ")
fruta2=input("digite o nome da segunda fruta: ")
fruta3=input("digite o nome da terceira fruta: ")

lista = [fruta1, fruta2, fruta3] 

random.shuffle(lista)
print("A ordem de apresentação da fruta será")
print(lista)