print("************************ For em uma lista ************************ ")
compras = ["arroz", "feijão", "macarrão", "carne"]
for i in compras:
    print("O item é: ", i)

print("************************ For em uma string ************************ ")
nome = "joaquim"
for i in nome:
    print("A letra é:", i)

print("************************ For em um dicionario ************************ ")
dicionario = {"index1": "Este é o item 1 do dicionario", "index2": "Este é o item 2 do dicionario"}
for i in dicionario:
    print("O index do dicionário é: ", i)
    print("O valor do dicionário é: ", dicionario[i])

print("************************ For em uma lista com listas ************************ ")
lista = [["arroz", "feijão", "macarrão"], ["carne", "frango", "peixe"], ["leite", "iogurte"]]
for i in lista:
    print("Item da lista com listas: ", i)


print("************************ For em uma lista aninhada ************************ ")
for i in lista:
    #print("Item da lista aninhada: ", i)
    for item in i:
        print("Item da lista aninhada: ", item)

print("************************ For com range ************************ ")
for i in range(0, 11):
    print("O Item do range é: ", i)

print("************************ For com range - contagem regressiva ************************ ")
for i in range(0, 11):
    print("O Item do range regressivo é: ", 10-i)
