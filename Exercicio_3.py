import json

def calcula_faturamento(vetor):
    # Inicializa as variáveis do menor e maior faturamento com o primeiro valor do vetor
    menor = vetor[0]
    maior = vetor[0]
    # Calcula a média mensal de faturamento
    media = sum(vetor) / len(vetor)
    # Inicializa a variável do número de dias com faturamento superior à média mensal
    num_dias = 0
    for valor in vetor:
        # Atualiza o valor do menor faturamento, se necessário
        if valor < menor:
            menor = valor
        # Atualiza o valor do maior faturamento, se necessário
        if valor > maior:
            maior = valor
        # Verifica se o valor do faturamento é superior à média mensal
        if valor > media:
            num_dias += 1
    # Retorna o menor faturamento, o maior faturamento e o número de dias com faturamento superior à média mensal
    return menor, maior, num_dias

with open('dados.json') as arquivo:
    dados = json.load(arquivo)
faturamento = int(dados['valor'])
print(faturamento)
menor, maior, num_dias = calcula_faturamento(faturamento)
print("Menor faturamento diário:", menor)
print("Maior faturamento diário:", maior)
print("Número de dias com faturamento superior à média mensal:", num_dias)