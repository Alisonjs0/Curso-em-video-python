soma = 0
cont = 0
while True:
    n = int(input("Digite um valor [999 para parar]: "))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"Foram digitados um total de {cont} numeros, e a soma entre eles é igual a {soma}.")