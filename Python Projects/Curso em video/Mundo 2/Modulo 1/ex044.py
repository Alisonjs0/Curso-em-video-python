valor = float(input("Digite o valor a ser pago: R$"))
pag = int(input("Qual a forma de pagamento?\n"
                "Digite [1] para à vista dinheiro/cheque\n"
                "Digite [2] para à vista no cartão\n"
                "Digite [3] para em até 2x no cartão\n"
                "Digite [4] para 3x ou mais no cartão:\n"
                "Qual é a opção? "))
if pag == 1:
    print(f"O valor a ser pago vai ser de R${valor* 0.9:.2f}")
elif pag == 2:
    print(f"O valor a ser pago vai ser de R${valor * 0.95:.2f}")
elif pag == 3:
    print(f"O valor a ser pago vai ser de R${valor:.2f}")
elif pag == 4:
    parc = int(input("Quantas parcelas? "))
    print(f"sua compra sera parcelda em {parc}x de {valor * 1.2 / parc:.2f} COM JUROS")
    print(f"O valor a ser pago vai ser de R${valor * 1.2:.2f}")