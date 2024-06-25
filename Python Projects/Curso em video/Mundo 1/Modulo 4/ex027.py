nome = input("Digite seu nome completo: ")
nome = nome.title().strip().split()
print(f"Seu nome completo é: {" ".join(nome)}.\n"
      f"Seu primeiro nome é: {nome[0]}.\n"
      f"Seu ultimo nome é: {nome[-1]}")
