somaAnos = 0
contMulher = 0
nomeVelho = ''
idadeVelho = 0

for i in range(4):
    print(f"----- {i+1}° PESSOA -----")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper().strip()
    somaAnos += idade

    if sexo == 'M' and idade > idadeVelho:
        nomeVelho = nome
        idadeVelho = idade

    if sexo == 'F' and idade < 20:
        contMulher += 1

print(f"A média de idade do grupo é: {somaAnos / 4}")
print(f"O nome do homem mais velho é {nomeVelho} e ele tem {idadeVelho}")
print(f"Tem {contMulher} mulheres abaixo dos 20 anos")