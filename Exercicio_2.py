# Função que verifica se um número pertence à sequência de Fibonacci
def pertence_fibonacci(num):
    # Caso base: os dois primeiros números da sequência são 0 e 1
    fib1 = 0
    fib2 = 1

    # Verifica se o número é igual a um dos dois primeiros números da sequência
    if num == fib1 or num == fib2:
        return True

    # Verifica se o número pertence à sequência a partir do terceiro número
    while fib2 < num:
        temp = fib2
        fib2 = fib1 + fib2
        fib1 = temp
        if fib2 == num:
            return True

    # Caso o número não pertença à sequência, retorna False
    return False

# Função principal que recebe um número como entrada e verifica se ele pertence à sequência de Fibonacci
def main():
    num = int(input("Digite um número: "))
    if pertence_fibonacci(num):
        print(num, "pertence à sequência de Fibonacci.")
    else:
        print(num, "não pertence à sequência de Fibonacci.")

# Executa a função principal
main()