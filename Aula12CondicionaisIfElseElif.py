# Condicionais If Else Elif parte 01
numero = input("Digite sua idade: ")

if float(numero) == 18 :
    print("O número é 18")
elif float(numero) > 18:
    print("Você é maior de idade")
elif float(numero) < 18:
    print("Você é menor de idade")
else:
    print("Essa não é uma idade válida")

idade = float(input("Digite sua idade: "))
sexo = input("Digite o sexo M ou F: ").lower()

if idade < 18 and sexo == "m":
    print("Homem menor de idade")
elif idade >= 18 and sexo == "m":
    print("Homem maior de idade")
elif idade < 18 and sexo == "f":
    print("Mulher menor de idade")
elif idade >= 18 and sexo == "f":
    print("Mulher maior de idade")
else:
    print("Erro na entrada de dados")