cidade = input("Digite o nome da cidade: ")
cidade = cidade.title().strip()

if cidade.find("Santo") == -1:
    print("Sua cidade não começa com Santo")
else:
    print("Sua cidade começa com Santo")