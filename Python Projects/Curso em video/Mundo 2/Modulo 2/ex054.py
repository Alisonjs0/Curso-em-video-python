n = 0
cont = 0
cont2 = 0
for i in range(7):
    n += 1
    ano = int(input(f"Em que ano a {n}° pessoa nasceu? "))
    if 2024 - ano <= 18:
        cont += 1
    else:
        cont2 += 1
print(f"{cont} pessoas ainda não atingiram a maioridade")
print(f"{cont2} pessoas já são maiores de idade")

