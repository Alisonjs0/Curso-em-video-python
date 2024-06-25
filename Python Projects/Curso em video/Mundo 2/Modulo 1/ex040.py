import numpy
notas = [
    float(input('Digite a primeira nota: ')),
    float(input("Digite a segunda nota: "))
]
media = numpy.mean(notas)
print(f"A media do aluno foi {media}")
if media < 5:
    print("O aluno esta REPROVADO!!")
elif media >= 5 and media < 7:
    print("O aluno esta em RECUPERAÇÂO!!")
else:
    print("O aluno foi APROVADO!!!")
