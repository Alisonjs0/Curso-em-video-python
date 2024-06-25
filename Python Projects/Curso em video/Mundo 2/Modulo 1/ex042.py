r1 = float(input("Digite o valor em CM da Primeira reta: "))
r2 = float(input("Digite o valor em CM da Segunda reta: "))
r3 = float(input("Digite o valor em CM da Terceira reta: "))
if r1 == r2 == r3:
    print("Esse tirangulo é EQUILÁTERO")
elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
    print('Esse triangulo é ISÓSCELES')
else:
    print("Esse triangulo é ESCALENO")