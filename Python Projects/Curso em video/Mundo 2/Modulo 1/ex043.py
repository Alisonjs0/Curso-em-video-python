alt = float(input("Digite sua altura (m): "))
peso = float(input("Digite seu peso (Kg): "))
imc = peso / alt**2
print(f"Seu imc é igual a: {imc:.1f}")
if imc < 18.5:
    print("Abaixo do Peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")