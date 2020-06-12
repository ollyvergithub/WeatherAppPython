# Tupla - São imutáveis
meses = ("janeiro", "Feveveiro", "Março", "Abril", "Maio", "junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
print("Meses do ano: ", meses)
print("O tipo da variável meses é: ", type(meses))

# Lista - São mutaveis
alunos = ["João", "Maria", "Pedro"]
print("Alunos: ", alunos)

print("O tipo da variável alunos é: ", type(alunos))
print("O tamanho de meses é: ", len(meses))
print("O tamanho de alunos é: ", len(alunos))
print("Acessando meses por indice: ", meses[0], meses[11])

# Alterando dados da lista
print("Alunos: ", alunos)
alunos[1] = "Ollyver"
print("Alunos: ", alunos)

# Adicionando a lista
alunos.append("Pietra")
print("Alunos: ", alunos)
alunos.insert(0, "Susi")
print("Alunos: ", alunos)

# Ordenando
alunos.sort()
print("Alunos: ", alunos)

# Retirando
alunos.pop() # Remove do fim
print("Alunos: ", alunos)
alunos.pop(0) # Remove o indice
print("Alunos: ", alunos)
alunos.remove("Pedro")
print("Alunos: ", alunos)

# Concatenando
alunos2 = ["Joana", "Jorge"]
total_de_alunos = alunos + alunos2
print("Alunos Concatenando Listas: ", total_de_alunos)