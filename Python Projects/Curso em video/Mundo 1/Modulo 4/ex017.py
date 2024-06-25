import math

co = float(input("Medida do cateto oposto: "))
ca = float(input("Medida do cateto adjacente: "))
h2 = co*co + ca*ca
h = math.sqrt(h2)

print(f"Comprimento do cateto oposto: {co}\n"
      f"Comprimento do cateto adjacente: {ca}\n"
      f"A hipotenusa vai medir: {h:.2f}")