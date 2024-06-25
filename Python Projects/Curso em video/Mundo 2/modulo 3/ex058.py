import win32com.client as win32
from random import randint
n = randint(1,100)
print("Sou eu seu computador...\n"
      "Acabei de pensar em um numero entre 0 e 100.\n"
      "Será que voce consegue adivinhar qual foi?")
meuN = 1
cont = 0
while meuN != n:
    meuN = int(input("Qual seu palpite? "))
    cont += 1
    if meuN > n:
        print("Menos... Tente novamente: ")
    elif meuN < n:
        print("Mais... Tente novamente: ")
print(f"Parabens, você acertou!!!\n"
      f"O numero escolhido era: {n}\n"
      f"Numero de tentativas: {cont}")