#   Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima
#   uma sequência em P.G. contendo 10 valores.

n1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
print("Os 10 primeiros termos dessa PG são: ")

for i in range(10):
    termo = n1 * r ** i
    print(termo, end=(" "))