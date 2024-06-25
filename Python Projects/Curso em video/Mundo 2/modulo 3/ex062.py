print("="*32,'\n',
      "      10 TERMOS DE UMA PA      \n",
      "="*32)
n1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
c = 1
quant = 1
while quant != 0:
    while c <= 10:
        print(n1, end=" -> ")
        n1 += r
        c += 1
    print("PAUSA")
    quant = int(input("Quantos termos você quer mostrar mais? "))
    if quant != 0:
        c2 = 1
        while c2 <= quant:
            print(n1, end=" -> ")
            n1 += r
            c2 += 1
    else:
        break
print('ACABOU!')