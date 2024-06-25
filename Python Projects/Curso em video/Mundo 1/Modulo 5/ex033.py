a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = int(input("Digite outro numero: "))
menor = a
maior = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"O menor valor digitado foi: {menor}\n"
      f"O maior valor digitado foi: {maior}")
