sexo = input("Digite o sexo [M/F]: ").strip()[0]
while sexo not in 'MmFf':
    sexo = input("Valor invalido, digite outro [M/F]: ").strip()[0]
print("Valor correto")