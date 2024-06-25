n1 = int(input('Digite um numero entre (0) e (9999): '))
if n1 > 0 and n1 < 10000:
    if n1 >= 0 and n1 < 10:
        n1 = str(n1)
        print(f"Unidade: {n1[0]}")
    elif n1 >= 10 and n1 < 100:
        n1 = str(n1)
        print(f"Unidade: {n1[1]}\n"
              f"Dezena: {n1[0]}")
    elif n1 >= 100 and n1 < 1000:
        n1 = str(n1)
        print(f"Unidade: {n1[2]} \n"
              f"Dezena: {n1[1]} \n"
              f"Centena: {n1[0]}")
    elif n1 >= 1000:
        n1 = str(n1)
        print(f"Unidade: {n1[3]} \n"
              f"Dezena: {n1[2]} \n"
              f"Centena: {n1[1]} \n"
              f"Milhar: {n1[0]}")

