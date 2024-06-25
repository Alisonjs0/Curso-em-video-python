largura = float(input("Quantos M de largura tem sua parede? "))
altura = float(input("Quantos M de altura tem sua parede? "))
litros = largura * altura / 2
print(f"Sua parede tem as dimensoes de {largura}x{altura} e sua area é de {(largura*altura):.2f}m² \n"
      f"Para pintar essa parede voce precisara de de {litros:.2f}l de tinta")