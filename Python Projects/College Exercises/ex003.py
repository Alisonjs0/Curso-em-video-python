#   Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima
#   uma sequência em P.A. contendo 10 valores.


n1 = float(input("Digite o primeiro termo: "))
n2 = float(input("Digite a razão: "))
print("Os 10 primeiros termos da progressão: ")
for i in range(10):
    termo = n1 + i * n2
    print(termo, end=(" "))