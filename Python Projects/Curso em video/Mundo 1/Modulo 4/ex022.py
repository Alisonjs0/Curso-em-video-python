n = input("Digite seu nome: ")
nome = n.strip()
espacos = nome.split()
print(f"Seu nome com maiusculas é: {nome.upper()}\n"
      f"Seu nome com minusculas é: {nome.lower()}\n"
      f"Seu nome ao todo tem: {len(''.join(espacos))} letras\n"
      f"Seu primeiro nome tem {len(espacos[0])}")
