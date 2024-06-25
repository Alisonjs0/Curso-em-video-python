from random import shuffle

alunos = [
    input("Primeiro aluno: "),
    input("Segundo aluno: "),
    input("Terceiro aluno: "),
    input("Quarto aluno: ")
]
shuffle(alunos)
print(f"A ordem de apresentação sera: \n"
      f"{alunos}")