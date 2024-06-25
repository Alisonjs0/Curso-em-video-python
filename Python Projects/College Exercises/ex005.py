#   Escreva um algoritmo que leia um valor inicial A e imprima a sequência de
#   valores do cálculo de A! (Fatorial) e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2
#   X 1 = 120


A = int(input("Digite o valor de (A): "))
total = 1
print(f"{A}! = ", end=(" "))
for i in range(A, 0, -1):
    total *= i
    if i > 1:
        print(f"{i} X",end=(" "))
    else:
        print(f"{i} = ",end=(""))
print(total)
