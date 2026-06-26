#Considere listas de listas e números. Cada lista, por sua vez, está formada por listas e números, recursivamente. Defina uma função achatar que retorne uma lista plana com todos os números da lista original. Por exemplo, achatar([1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]) deverá retornar [1, 2, 4, 2, 5, 2, 1, 2, 3, 1, 8]. Dê duas versões, uma sem compreensões e outra com compreensões. A versão com compreensões não precisa retornar os elementos na ordem em que aparecem os números de esquerda à direita.
def achatar_comp(lista):
    return [n for item in lista
              for n in (achatar_comp(item) if type(item) == list else [item])]
lista1 = input("Insira a lista que deseja achatar")
print(achatar_comp(lista1))

