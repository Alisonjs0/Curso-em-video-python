r = int(input("Quantos termos você quer mostrar? "))
cont = 0
n1 = 0
n2 = 1
n3 = 0
print(f"{n1} -> {n2} ->", end=" ")
while cont <= r - 3:
    cont += 1
    print(n1 + n2, end=" -> ")
    n3 = n1
    n1 = n2
    n2 += n3
print("FIM")