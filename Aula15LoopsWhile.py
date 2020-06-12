# Aula 15 Loops - While

contador = 0

while contador < 5:
    print("Contador: ", contador)
    contador += 1
else:
    print("Fim do while - contador: ", contador)

pessoas = []
x = 0
while x < 4 and "Julia" not in pessoas:
    nome = input("Qual o seu nome? ")
    pessoas.append(nome)
    print(pessoas)
    x +=1
else:
    print("O total de pessoas é: ", pessoas)

pessoas = []
x = 0
while x < 4:
    nome = input("Digite seu nome: ")
    if nome == 'joao':
        continue
    pessoas.append(nome)
    x += 1

print("As pessoas são: ", pessoas)


