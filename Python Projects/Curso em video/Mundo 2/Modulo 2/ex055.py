from numpy import max
from numpy import min
lista = []
for i in range(5):
    peso = float(input(f"Digite o peso da {i+1}° pessoa: "))
    lista.append(peso)
print(f"O maior peso liso foi: {max(lista):.2f}Kg")
print(f"O menor peso liso foi: {min(lista):.2f}Kg")