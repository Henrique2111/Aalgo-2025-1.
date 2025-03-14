import time
import random

def quick_sort(arr):
    """Função que implementa o algoritmo Quick Sort."""
    if len(arr) <= 1:
        return arr  # Caso base: lista já ordenada ou vazia
    else:
        pivot = arr[len(arr) // 2]  # Escolhendo o pivô como o elemento central
        left = [x for x in arr if x < pivot]  # Elementos menores que o pivô
        middle = [x for x in arr if x == pivot]  # Elementos iguais ao pivô
        right = [x for x in arr if x > pivot]  # Elementos maiores que o pivô
        return quick_sort(left) + middle + quick_sort(right)  # Recursão

def medir_tempo_execucao(tamanho):
    """Gera uma lista aleatória e mede o tempo de execução do Quick Sort."""
    arr = [random.randint(0, 1000000) for _ in range(tamanho)]  # Lista aleatória
    inicio = time.perf_counter()  # Tempo inicial com alta precisão
    quick_sort(arr)  # Ordenação
    fim = time.perf_counter()  # Tempo final
    return fim - inicio  # Tempo total

# Medindo tempos para diferentes tamanhos de entrada
tamanhos = [100, 1000, 10000, 100000]
resultados = {tamanho: medir_tempo_execucao(tamanho) for tamanho in tamanhos}

# Exibindo os tempos de execução
for tamanho, tempo in resultados.items():
    print(f"Tempo para ordenar {tamanho} elementos: {tempo:.6f} segundos")
