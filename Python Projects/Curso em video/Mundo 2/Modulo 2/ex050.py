soma = 0
cont = 0
for i in range(1, 7, 1):
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f"Dos 6 numeros digitados {cont} foram pares, e a soma entre eles é igual a: {soma}")