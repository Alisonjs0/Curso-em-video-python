import math

angulo = float(input("Digie o valor do angulo: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f"O angulo de {angulo}° tem o seno de: {sen:.2f}\n"
      f"O angulo de {angulo}° tem o coseno de {cos:.2f}\n"
      f"O angulo de {angulo}° tem a tangente de {tan:.2f}")
