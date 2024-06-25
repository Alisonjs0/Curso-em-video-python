nome = input("Digite seu nome completo: ")
nome = nome.title().strip()
if nome.find('Silva') != -1:
    nome = nome.split()
    print(f"O usuario {nome[0]} tem (Silva) no nome")
else:
    nome = nome.split()
    print(f"O usuario {nome[0]} não tem (Silva) no nome")
