print("="*32,'\n',
      "      10 TERMOS DE UMA PA      \n",
      "="*32)
n1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
c = 1
while c <= 10:
    print(n1, end=" -> ")
    n1 += r
    c += 1
print('ACABOU!')