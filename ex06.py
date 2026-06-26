#Contar vogais em uma string
def contar_vogais(texto):
    return sum([1 for letra in texto if letra in "aeiou"])
print(contar_vogais("Samba"))