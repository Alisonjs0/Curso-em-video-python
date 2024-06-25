salario = float(input("Digite seu salario: R$"))
if salario > 1250:
    salario *= 1.1
    print(f"Seu salario teve um aumento de 10% e agora ele é de: R${salario:.2f}")
else:
    salario *= 1.15
    print(f"Seu salario teve um aumento de 15% e agora ele é de: R${salario:.2f}")