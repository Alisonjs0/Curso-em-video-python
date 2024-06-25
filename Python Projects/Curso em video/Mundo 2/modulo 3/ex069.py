maiores = 0
homens = 0
mulheresmenosvinte = 0
while True:
    print("-"*27)
    print("    CADASTRE UMA PESSOA    ")
    print("-"*27)
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [H/M] ").strip().upper()[0])
    if idade > 18:
        maiores+= 1
    if sexo in "Hh":
        homens+=1
    if sexo in "Mm" and idade < 20:
        mulheresmenosvinte+= 1
    print("-"*27)
    prox = str(input("Quer continuar? [S/N]: ").strip().upper()[0])
    if prox in "Nn":
        break
print(f"Tem {maiores} pessoas com mais de 18 anos.\n"
      f"Foram cadastrados {homens} homens.\n"
      f"Tem {mulheresmenosvinte} com menos de 20 anos")