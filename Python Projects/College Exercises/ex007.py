#   Faça um programa que leia um número n e mostre na tela os n primeiros
#   números pares e depois os n primeiros números ímpares

n = int(input("Digite o valor de (N): "))
print(f"Proximos {n} números pares: ",end=(" "))
for i in range(n, n+n*2, 1):
    if i % 2 == 0:
        print(i,end=(" "))
print("")
print(f"Proximos {n} números ímpares: ",end=(" "))
for a in range(n, n+n*2, 1):
    if a % 2 == 1:
        print(a, end=(" "))
