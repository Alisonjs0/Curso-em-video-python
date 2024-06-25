from datetime import date
ano = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - ano
print(f"Voce tem {idade} anos.")
if idade <= 9:
    print("Voce esta na categoria MIRIM")
elif idade <= 14:
    print("Voce esta na categoria INFANTIL")
elif idade <= 19:
    print("Voce esta na categoria JUNIOR")
elif idade <= 25:
    print("Voce esta na categoria SENIOR")
else:
    print("Voce esta na categoria MASTER")