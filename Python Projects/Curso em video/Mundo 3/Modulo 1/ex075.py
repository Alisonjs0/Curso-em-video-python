pares = ''
num = (
    int(input('Digite um valor: ')),
    int(input('Digite outro: ')),
    int(input('Digite outro: ')),
    int(input('Digite outro: '))
)

print(f'O numero 9 aparece {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 foi digitado na posição {num.index(3)+1}.')
else:
    print('O valor 3 não foi digitado.')
print(f"Os numeros pares são: ", end='')
for n in num:
    if n % 2 == 0:
        pares += str(n)
        if len(pares) < 4:
            print(n, end=', ')
        else:
            print(n, end='.')

'''produtos = [("Produto A", 10), ("Produto B", 20), ("Produto C", 30)]

for produto, preco in produtos:
    print('%-15s R$%.2f' % (produto, preco))'''