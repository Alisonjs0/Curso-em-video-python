a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
sinal = (str(input("Digite o sinal (+ soma) (- subtração) (* multiplicação) (/ divisão) ")))

if sinal == "+":
    print(a+b)
elif sinal == "-":
    print(a-b)
elif sinal == "*":
    print(a*b)
elif sinal == "/":
    print(a/b)