#    Faça um programa que leia vários inteiros positivos e mostre, no final, a
#   soma dos números pares e a soma dos números ímpares. O programa
#   para quando entrar um número maior que 1000.

def teste():
    numPar = 0
    numImpar = 0
    n = 0
    while True:
        n = int(input("Digite um valor: "))
        if n > 1000:
            break
        if n % 2 == 0:
            numPar += n
        elif n % 2 ==1:
            numImpar += n
    print(f"Soma dos números pares: {numPar}")
    print(f"Soma dos números ímpares: {numImpar}")

teste()