n1 = int(input("Digite um numero: "))
cont = 0
for i in range(1, n1+1, 1):
    if n1 % i == 0:
        print(f"\033[1;49;32m{i}\033[m", end=" ")
        cont += 1
    else:
        print(f"\033[1;49;31m{i}\033[m", end=" ")
print('')
print(f"O numero {n1} foi divisivel {cont} vezes")
if cont == 2:
    print("E por isso ele É PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")