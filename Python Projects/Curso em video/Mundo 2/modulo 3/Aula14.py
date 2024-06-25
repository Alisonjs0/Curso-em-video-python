n = 1
par = 0
impar = 0
total = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        total += 1
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Foram digitados {total} numeros, {par} pares e {impar} impares")