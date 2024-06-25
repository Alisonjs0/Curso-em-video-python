from random import randint
from time import sleep
maq = randint(1,3)
jogo = int(input("Escolha sua jogada:\n"
                 "[1] para Papel\n"
                 "[2] para Pedra\n"
                 "[3] para Tesoura\n"
                 "Digite sua opção: "))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')

print('-=' * 11)

if jogo == 1:
    print("Você escolheu Papel")
elif jogo == 2:
    print("Você escolheu Pedra")
elif jogo == 3:
    print("Você escolheu Tesoura")
else:
    print("Jogada invalida")

if jogo <= 3 and jogo >= 1:
    if maq == 1:
        print("O computador escolheu Papel")
    elif maq == 2:
        print("O computador escolheu Pedra")
    else:
        print("O computador escolheu Tesoura")

    if maq == jogo:
        print("\033[1;49;33mEMPATARAM!!\033[m")
    elif (maq == 1 and jogo == 2) or (maq == 3 and jogo == 1) or (maq == 2 and jogo == 3):
        print("\033[1;49;31mCOMPUTADOR VENCEU!!\033[m")
    else:
        print("\033[1;49;32mVOCE VENCEU\033[m")

print('-=' * 11)