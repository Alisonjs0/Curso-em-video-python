frase = "Curso em Video Python."
print(frase[9])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print(len(frase))   # Quantidade de Caracteres
print(frase.count("o", 0, 14))   # Quantidade de Caracteres especificos
print(frase.find("deo"))     # Procurar dentro da string
print(frase.find('Android'))     # Procurar dentro da string
print('Curso' in frase)     # Procurar dentro da string
print(frase.replace('o', 'e'))  # trocar caracteres
print(frase.upper())    # tudo maiusculo
print(frase.lower())    # tudo minusculo
print(frase.capitalize())   # Primeira letra maiuscula
print(frase.title())    # Primeira letra de cada palavra em maiusculo
print(frase.split())    # Repartir string
frase3 = frase.split()
print('-'.join(frase3)) # Juntar string

frase2 = '   Aprenda Python  '
print(frase2)
print(frase2.strip())   #   Eliminar espaços indevidos
print(frase2.rstrip())
print(frase2.lstrip())