#par de uma matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
pares_matriz = [n for linha in matriz for n in linha if n % 2 == 0]
print(pares_matriz)

