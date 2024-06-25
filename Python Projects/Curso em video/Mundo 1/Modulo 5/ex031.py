km = float(input("Digite a distancia em KM: "))
if km < 200:
    print(f"O valor da viagem de {km}KM é de R${km*0.5:.2f}")
else:
    print(f"O valor da viagem de {km}KM é de R${km*0.45:.2f}")