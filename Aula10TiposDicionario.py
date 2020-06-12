# Dicionarios - São acessados por keys igual a um array multidimensional
pessoa = {"nome": "João", "sobrenome": "Pereira", "profissao": "Desenvolvedor", "filhos": ['Pedro', 'Maria']}
print(pessoa)
print("O tipo da variável pessoa é: ", type(pessoa))
print("O sobrenome da pessoa é: ", pessoa["sobrenome"])
print("Os filhos da pessoa: ", pessoa["filhos"])
print("Um determinado filho: ", pessoa["filhos"][0])

# Operações
# Tamanho
print("O tamanho de pessoa é: ", len(pessoa))

# Apagando
del pessoa["filhos"]
print("O tamanho de pessoa é: ", len(pessoa))

# Mudando
pessoa["profissao"] = "Analista"
print(pessoa)

# Se possui chave específica
print("sobrenome" in pessoa)

print("*********************************")

# Loop
for x in pessoa:
    print(x)
print("*********************************")

for x in pessoa:
    print(x+": "+pessoa[x])

print("*********************************")

# Get
print(pessoa.get("nome", "Esta informação nao consta no cadastro"))
print(pessoa.get("filhos", "Esta informação nao consta no cadastro"))
print("*********************************")

pessoa["filhos"] = ['Pedro', "Maria"]
pessoa["filhos"].append("Jorginho")
print(pessoa)
print("*********************************")

# Apagando
pessoa.clear()
print(pessoa)



