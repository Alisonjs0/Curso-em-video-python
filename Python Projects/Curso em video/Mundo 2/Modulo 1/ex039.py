from datetime import date
data = int(input("Digite em que ano vc nasceu: "))
idade = date.today().year - data
if idade < 18:
    print(f"Você ainda não pode se alistar, faltam {18 - idade} anos.")
elif idade == 18:
    print(f"Voce está no momento exato para se alistar.")
elif idade > 18:
    print(f"Você ainda pode se alistar, mas já se passaram {idade - 18} anos.")