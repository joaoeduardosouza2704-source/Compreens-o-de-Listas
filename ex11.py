def acima_media(notas):
    return sum([1 for nota in notas if nota > 5])
notas = [3,5,6,7,8]
print(acima_media(notas))