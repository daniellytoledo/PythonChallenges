import random
import time
lista = ["pedra", "papel", "tesoura"]
print("-"*49)
print("-"*20, "\033[1;7mJOKENPÔ\033[m", "-"*20)
print("-"*49)
print(" \033[1mO COMPUTADOR ESCOLHEU PEDRA, PAPEL OU TESOURA...\033[m")
print("-"*49)
R = str(input("\033[1mSUA VEZ!\033[m Escreva pedra, papel ou tesoura: "))
print("\033[34m-\033[m"*20, "\033[1;7mJO\033[m")
time.sleep(0.5)
print("\033[34m-\033[m"*33, "\033[1;7mKEN\033[m")
time.sleep(0.5)
print("\033[34m-\033[m"*45, "\033[1;7mPÔ!\033[m")
time.sleep(0.5)
C = random.choice(lista)
if R == C:
    print("Respostas iguais. Tente de novo.")
elif R == "pedra" and C == "papel":
    print("\033[1;31mVOCÊ PERDEU\033[m! O computador escolheu {}.".format(C))
elif R == "papel" and C == "pedra":
    print("\033[1;32mVOCÊ GANHOU\033[m! O computador escolheu {}.".format(C))
elif R == "tesoura" and C == "papel":
    print("\033[1;32mVOCÊ GANHOU\033[m! O computador escolheu {}.".format(C))
elif R == "papel" and C == "tesoura":
    print("\033[1;31mVOCÊ PERDEU\033[m! O computador escolheu {}.".format(C))
elif R == "tesoura" and C == "pedra":
    print("\033[1;31mVOCÊ PERDEU\033[31m! O computador escolheu {}.".format(C))
elif R == "pedra" and C == "tesoura":
    print("\033[1;32mVOCÊ GANHOU\033[m! O computador escolheu {}.".format(C))
print("-"*16, "\033[1mJOGO ENCERRADO\033[m!", "-"*16)
