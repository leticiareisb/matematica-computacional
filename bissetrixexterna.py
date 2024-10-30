def razao_bissetriz_externa(a, b, c):
    return b / (b + c)

a = float(input("Digite o comprimento do lado a (oposto ao ângulo A): "))
b = float(input("Digite o comprimento do lado b (adjacente ao ângulo A): "))
c = float(input("Digite o comprimento do lado c (adjacente ao ângulo A): "))

print("Razão formada pela bissetriz externa no lado oposto:", razao_bissetriz_externa(a, b, c))
