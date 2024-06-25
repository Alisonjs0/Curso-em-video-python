n1 = int(input("Digite um numero para calcular seu fatorial: "))
fat = 1
print(f"Calculando {n1}! =", end=" ")
while n1 != 0:
    print(f"{n1}", end=" ")
    if n1 > 1:
        print("X",end=" ")
    fat *= n1
    n1 -= 1
print(f"= {fat}")