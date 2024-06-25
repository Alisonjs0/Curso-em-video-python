import math
import random
n2 = random.randint(1,10)
print(n2)
n1 = int(input("Digite o valor de n1: "))
print(f"Arredondamento pra cima: {math.ceil(n1)}")
print(f"Arredondamento pra baixo: {math.floor(n1)}")
print(f"Eliminar numeros após a virgula: {math.trunc(n1)}")
print(f"Potencia: {math.pow(n1, 2)}")
print(f"Raiz quadrada: {math.sqrt(n1):.2f}")
print(f"Fatorial: {math.factorial(n1)}")