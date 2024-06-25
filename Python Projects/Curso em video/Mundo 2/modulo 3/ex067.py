while True:
    cont = 1
    n = int(input("Quer ver a tabuada de qual valor? "))
    if n < 0:
        break
    print("-" * 15)
    for i in range(10):
        print(f"{n} x {cont} = {n*cont}")
        cont += 1
    print("-" * 15)
print("PROGRAMA DE TABUADA ENCERRADO. Volte sempre!")