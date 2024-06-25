lanche = ("hamburguer", "Suco", "Pizza", "Pudim")
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")
print(lanche[-1])
for c in lanche:
    print(c,end=", ")
print("\n")
for pos, comida in enumerate(lanche):
    print(f"Vou comer {comida} na posição {pos}")