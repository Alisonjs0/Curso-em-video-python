classificacao = ("Palmeiras", "Internacional", "Fluminense", "Corinthians", "Flamengo",
"Athletico-PR", "Atlético-MG", "Fortaleza", "São Paulo", "América-MG",
"Botafogo", "Santos", "Goiás", "Bragantino", "Coritiba",
"Cuiabá", "Ceará", "Atlético-GO", "Avaí", "Juventude")

print(f"Os 5 primeiros colocados são: {classificacao[:6]}")
print(f"Os 4 ultimos 4 colocados são: {classificacao[-4:]}")
print(f"Em ordem alfabetica: {sorted(classificacao)}")
print(f"Santos esta em {classificacao.index('Santos')+1}° na classificação")