from time import sleep

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
op = 1

while op != 5:
    print("[ 1 ] Somar \n"
          "[ 2 ] Multiplicar \n"
          "[ 3 ] Maior \n"
          "[ 4 ] Novos números \n"
          "[ 5 ] Sair do programa")
    op = int(input(">>>>> Qual é a sua opção? "))
    if op == 1:
        print(f"A soma entre {n1} e {n2} é {n1 + n2}")
    elif op == 2:
        print(f"A multiplicação entre {n1} e {n2} é {n1 * n2}")
    elif op == 3:
        if n1 > n2:
            print(f"Entre {n1} e {n2} o maior é {n1}")
        elif n2 > n1:
            print(f"Entre {n1} e {n2} o maior é {n2}")
        else:
            print(f"Os valores são iguais")
    elif op == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif op == 5:
        break
    else:
        print("Valor invalido, tente novamente")
    print("=-="*16)
    sleep(1.5)