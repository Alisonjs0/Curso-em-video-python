casa = float(input("Qual valor da casa? R$"))
sal = float(input("Qual o Salario do comprador? R$"))
anos = int(input("Em qunatos anos ele vai pagar? "))
parc = casa / (12*anos)
print(f"Para pagar a casa de R${casa:.2f} em {anos} anos a prestação minima será de R${parc:.2f}")
print(f"Comparando tem que pagar R${parc:.2f} e o minimo é R${sal * 0.3:.2f}")
if parc <= (sal*0.3):
    print("Emprestimo concedido!!!")
else:
    print('Emprestimo NEGADO!!!')