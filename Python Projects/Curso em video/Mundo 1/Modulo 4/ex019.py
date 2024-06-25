import random

alunos = [
    input("Primeiro aluno: "),
    input("Segundo aluno: "),
    input("Terceiro aluno: "),
    input("Quarto aluno: ")
]

escolhido = random.choice(alunos)
print(f"O aluno escolhido foi: {escolhido}.")