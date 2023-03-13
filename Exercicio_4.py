def calcula_percentual_representacao(faturamento_estados):
    # Calcula o valor total mensal da distribuidora
    total = sum(faturamento_estados.values())
    # Cria um dicionário vazio para armazenar os percentuais de representação de cada estado
    percentuais = {}
    # Calcula o percentual de representação de cada estado e armazena no dicionário
    for estado, faturamento in faturamento_estados.items():
        percentuais[estado] = faturamento / total * 100
    # Retorna o dicionário com os percentuais de representação de cada estado
    return percentuais

# Exemplo de uso da função calcula_percentual_representacao
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
percentuais = calcula_percentual_representacao(faturamento_estados)
# Imprime o percentual de representação de cada estado
for estado, percentual in percentuais.items():
    print("Percentual de representação de", estado, ":", round(percentual, 2), "%")