from random import randint
cont = 0
while True:
    ncomp = randint(1,10)
    n = int(input("Diga um valor: "))
    parimp = str(input("Par ou impar? [P/I]: ").strip().upper()[0])
    print("-"*15)
    if (ncomp + n) % 2 == 0:
        result = "PAR"
    else:
        result = "IMPAR"
    print(f"Voce jogou {n} e o computador {ncomp}. Total de {n+ncomp} DEU {result}")
    print("-"*15)
    if result[0] == parimp:
        print("Você venceu!!\n"
              "Vamo jogar novamente...")
        print("=-=" * 10)
        cont+=1
    else:
        print("VOCE PERDEU!!")
        print("=-" * 15)
        break
print(f"GAME OVER!! Voce venceu {cont} vezes")