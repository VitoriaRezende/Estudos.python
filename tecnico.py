from random import randint, c

print("\033[1;33m-------------------------------------------\033[0m")

print("\033[33mVAMOS JOGAR IMPAR OU PAR\033[0m")

print("\033[1;33m-------------------------------------------\033[0m")

escolha=input("\033[33mEscolha entre impar ou par:\033[0m ").upper()
if escolha!="PAR" and escolha!="IMPAR":
    print("\033[31mOpção inválida, tente novamente!\033[0m")
    exit()
numero=randint(1,10) 
soma=numero+3
print("\033[33mO computador escolheu o numero {}\033[0m".format(soma))
if soma %2==0 and escolha=="PAR":
    print("\033[32mParabéns, você venceu!\033[0m")
elif soma %2!=0 and escolha=="IMPAR":
    print("\033[32mParabéns, você venceu!\033[0m")
else:
    print("\033[31mOps, infelizmente você perdeu!\033[0m")  
    
print("\033[1;33m-------------------------------------------\033[0m")
    


