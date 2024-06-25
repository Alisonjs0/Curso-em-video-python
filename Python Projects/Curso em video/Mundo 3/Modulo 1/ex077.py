palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')

for vog in palavras:
    print(f"\n Na palavra {vog} temos ", end='')
    for letra in vog:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')