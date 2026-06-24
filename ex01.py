#Defina uma função que leia do teclado uma sequência de números inteiros dados em uma única linha. A função deve retornar uma lista contendo os números que estão na linha.
def ler_inteiros():
    inteiros = [n for n in map(int,input().split())]
    return inteiros
print(ler_inteiros())