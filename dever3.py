# Função recursiva para verificar se um array é palíndromo
def verificar_palindromo(arr, inicio, fim):
    # Caso base: se o índice inicial for maior ou igual ao final, o array é palíndromo
    if inicio >= fim:
        return True
    
    # Se os elementos nas posições 'inicio' e 'fim' forem diferentes, não é um palíndromo
    if arr[inicio] != arr[fim]:
        return False
    
    # Chamada recursiva com o próximo par de elementos (movendo os índices para dentro)
    return verificar_palindromo(arr, inicio + 1, fim - 1)

# Função para iniciar a verificação de palíndromo
def eh_palindromo(arr):
    return verificar_palindromo(arr, 0, len(arr) - 1)

# Testando com diferentes arrays
test_cases = [
    [1, 2, 3, 2, 1],    # Palíndromo
    [1, 2, 3, 4, 5],    # Não é palíndromo
    [7, 8, 7],          # Palíndromo
    [10, 20, 30, 20, 10] # Palíndromo
]

for case in test_cases:
    resultado = eh_palindromo(case)
    print(f"O array {case} é palíndromo? {resultado}")
