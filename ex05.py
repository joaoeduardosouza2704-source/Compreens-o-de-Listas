#Dada uma lista com nomes, filtrar palavras maiores que 5 letras
nomes  = input().split()
nomes_maiores_5 = [nome for nome in nomes if len(nome) > 5]
print(nomes_maiores_5)