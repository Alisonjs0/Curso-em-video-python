c50 = 0
c20 = 0
c10 = 0
c1 = 0
while True:
    print("="*27)
    print("           BANCO")
    print("="*27)
    val = int(input("Qual valor será sacado? "))
    while val - 50 >= 0:
        val -= 50
        c50+=1
    if c50 > 0:
        print(f"Notas de 50: {c50}")
    while val - 20 >= 0:
        val -= 20
        c20+=1
    if c20 > 0:
        print(f"Notas de 20: {c20}")
    while val - 10 >= 0:
        val -= 10
        c10+=1
    if c10 > 0:
        print(f"Notas de 10: {c10}")
    while val - 1 >= 0:
        val -= 1
        c1+=1
    if c1 > 0:
        print(f"Notas de 1: {c1}")
    break
print("="*27)