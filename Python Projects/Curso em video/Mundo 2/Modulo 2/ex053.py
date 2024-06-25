frase = input("Dogite uma frase: ").strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
'''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
    
'''
if junto == inverso:
    print('Temos um palindromo!')
else:
    print("Nãp temos um palindromo!")
print(f"O inverso de {junto} é {inverso}")