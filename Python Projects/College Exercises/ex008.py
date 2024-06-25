#   Faça um programa que leia um número n e imprima se ele é primo ou
#   não. (um número primo tem apenas 2 divisores: 1 e ele mesmo! O
#   número 1 não é primo!!!)

def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Digite um número: "))

if primo(n):
    print(f"{n} é primo!")
else:
    print(f"{n} não é primo.")