import time

# Função iterativa para calcular o fatorial de um número n
def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Função para medir o tempo de execução
def medir_tempo_execucao(func, n):
    inicio = time.time()  # Marca o tempo inicial
    resultado = func(n)  # Chama a função
    fim = time.time()  # Marca o tempo final
    tempo_execucao = fim - inicio  # Calcula o tempo de execução
    return resultado, tempo_execucao

# Testando com diferentes valores de n
valores_n = [10, 100, 500, 1000]
for n in valores_n:
    resultado, tempo = medir_tempo_execucao(fatorial_iterativo, n)
    print(f"Fatorial de {n}: {resultado}")
    print(f"Tempo de execução para n={n}: {tempo:.8f} segundos\n")

