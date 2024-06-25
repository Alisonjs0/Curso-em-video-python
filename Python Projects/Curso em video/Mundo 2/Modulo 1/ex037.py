n = int(input("Digite um numero: "))
conv = int(input("Digite a base de conversão:\n"
                 "[1] BINARIO\n"
                 "[2] OCTAl\n"
                 "[3] HEXADECIMAL\n"
                 ))
if conv == 1:
    print(f"{n} convertido para BINARIO fica igual a: {bin(n)[2:]}")
elif conv == 2:
    print(f"{n} convertido para OCTAL é igual a {oct(n)[2:]}")
elif conv == 3:
    print(f"{n} convertido para HEX é igual a {hex(n)[2:].upper()}")
else:
    print("Valor invalido, tente novamente")