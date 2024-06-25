from random import randint
from time import sleep
n1 = randint(0,5)
print("Vou pensar em um numero, tente adivinhar qual é: ")
jogador = int(input("Digite um numero de 0 a 5: "))
print("Processando...")
sleep(2)
if n1 == jogador:
    print(f"Parabens, voce acertou o numero era: {n1}")
else:
    print(f"Infelizmente voce errou, o numero era: {n1}")