def inverte_string(string):
    # Converte a string em uma lista de caracteres
    lista_caracteres = list(string)
    # Obtém o índice do primeiro e último caracteres da string
    inicio = 0
    fim = len(lista_caracteres) - 1

    # Loop para trocar os caracteres da string
    while fim > inicio:
        # Troca o caractere no índice de início com o caractere no índice de fim
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        # Incrementa o índice de início e decrementa o índice de fim
        inicio += 1
        fim -= 1

    # Junta a lista de caracteres em uma string e retorna
    nova_string = "".join(lista_caracteres)
    return nova_string