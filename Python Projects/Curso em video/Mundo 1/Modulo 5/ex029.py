vel = float(input('Qual a velocidade atual do carro: '))
if vel > 80:
    print(f"Voce ultrapassou o limite de velocidade. \n"
          f"Multado em: R${(vel-80)*7:.2f}")
else:
    print(f"Voce esta dentro da velocidade permitida")