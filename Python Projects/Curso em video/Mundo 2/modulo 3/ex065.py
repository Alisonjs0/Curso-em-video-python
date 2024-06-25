soma = 0
n1 = 0
cont = 0
simn = ''.upper()
while simn != "N":
    n1 = int(input("Digite um numero: "))
    simn = str(input("Quer continuar? [S/N] ").upper().strip()[0])
    cont += 1
    soma += n1
    if cont == 1:
        maior = n1
        menor = n1
    if maior <= n1:
        maior = n1
    elif menor > n1:
        menor = n1
media = soma / cont
print(f"Voce digitou {cont} numeros e a media foi de {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")