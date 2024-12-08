import random
import time
G = ""
V = 0
print("-"*16, "\033[7mJOGO PAR OU ÍMPAR\033[m", "-"*16)
while True:
    if G == "perdeu":
        break
    N1 = int(input("Escolha um número de 0 até 5: "))
    print("[1] PAR")
    print("[2] ÍMPAR")
    P1 = int(input("Agora escolha par ou ímpar: "))
    N2 = random.randint(0,5)
    print("\033[7m- PAR \033[m")
    time.sleep(0.5)
    print("\033[7m----- OU \033[m")
    time.sleep(0.5)
    print("\033[7m-------- ÍMPAR \033[m")
    time.sleep(0.5)
    print("O computador escolheu {}.".format(N2))
    S = N1 + N2
    if S % 2 == 0 and P1 == 1:
        print("A soma dos dois números é PAR. Você ganhou!")
        G = "ganhou"
        V = V + 1
        print("-"*49)
    elif S % 2 == 0 and P1 == 2:
        print("A soma dos dois números é PAR. Você perdeu!")
        G = "perdeu"
        print("-" * 49)
    elif S % 2 != 0 and P1 == 1:
        print("A soma dos dois números é ÍMPAR. Você perdeu!")
        G = "perdeu"
        print("-" * 49)
    elif S % 2 != 0 and P1 == 2:
        print("A soma dos dois números é ÍMPAR. Você ganhou!")
        G = "ganhou"
        V = V + 1
        print("-" * 49)
print("Parabéns! Você perdeu agora, e ganhou {} partida(s) no total.".format(V))
