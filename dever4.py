def F(n):
    if n == 1:
        return 2
    return 2 * F(n - 1) + n**2

# Solicita ao usuário um valor de n
n = int(input("Digite um valor para n: "))

# Calcula e exibe o resultado
resultado = F(n)
print(f"F({n}) = {resultado}")
4