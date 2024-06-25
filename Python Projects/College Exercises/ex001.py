#   Faça um algoritmo estruturado que leia uma quantidade não determinada
#   de números positivos. Calcule a quantidade de números pares e ímpares,
#   a média de valores pares e a média geral dos números lidos. O número
#   que encerrará a leitura será zero.


def teste():
    numPositivo = 0
    numPar = 0
    numImpar = 0
    mediaPar = 0
    totalPar = 0
    mediaGeral= 0
    total = 0
    somaTotal = 0

    while True:
        numero = int(input("Digite um numero, ou digite [0] para sair: "))

        if numero == 0:
            break
        elif numero > 0:
            total += 1
            somaTotal += numero
            if numero % 2 == 0:
                totalPar += 1
                numPar += numero
            else:
                numImpar += 1
        else:
            print("Número inválido! Digite um número positivo ou 0 para sair.")
    if total == 0:
        print("Nenhum valor foi inserido")
    else:
        mediaGeral = somaTotal / total
        if totalPar > 0:
            mediaPar = numPar/ totalPar
        else:
            mediaPar = 0
    print(f"Quantidade de números: {total}")
    print(f"Quantidade de números pares: {totalPar}")
    print(f"Quantidade de números impares: {numImpar}")
    print(f"Média de números pares: {mediaPar}")
    print(f"Media Geral: {mediaGeral}")
teste()