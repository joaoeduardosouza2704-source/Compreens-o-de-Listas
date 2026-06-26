#Tamanha de cada palavra
def tamanho_cada_palavra(lista_palavras):
    return [len(palavra) for palavra in lista_palavras]
lista_palavras = list(input().split())
print(tamanho_cada_palavra(lista_palavras))