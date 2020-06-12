# Tipo de dados String
nome = "Ollyver"
sobrenome = "Ottoboni"
print("Meu nome é: ", nome)
print("O tipo da variável nome é: ", type(nome))
print("Meu sobrenome é: ", sobrenome)

# Concatenando
print("Meu nome completo é: ", nome+' '+sobrenome)

nome_completo = nome+' '+sobrenome

print("Repetindo nome completo 5 vezes: ", nome_completo*5)

print("Tamanho de nome completo: ", len(nome_completo))

print("Pegando a primeira letra do nome completo: ",nome_completo[0])

print("Pegando de tras pra frente: ",nome_completo[-1])

print("Fatiando a variavel: ",nome_completo[0:-1])

print("Fatiando a variavel: ",nome_completo[0:])