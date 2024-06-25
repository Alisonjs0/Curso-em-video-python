tot = 0
cont = 0
barato = 0
c = 0
nomebarato = ''
while True:
    nome = input("Digite o nome do produto: ")
    valor = float(input("Qual valor do produto: R$"))
    c+=1
    tot += valor
    if valor > 1000:
        cont += 1
    if c == 1:
        barato = valor
        nomebarato = nome
    if barato > valor:
        barato = valor
        nomebarato = nome
    prox = str(input("Deseja continuar? [S/N] ").strip().upper()[0])
    if prox in "Nn":
        break
print("--------- FIM DO PROGRAMA ---------")
print(f"Total gasto: {tot:.2f}. \n"
      f"Produtos acima de R$1000: {cont} \n"
      f"Produto mais barato: {nomebarato} custando R${barato:.2f}")