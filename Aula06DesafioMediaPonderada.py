nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
peso1 = float(input("Digite o valor da peso 1: "))
peso2 = float(input("Digite o valor da peso 2: "))

media_ponderada = ((peso1*nota1) + (peso2*nota2)) / (peso1+peso2)

print("A média ponderada é: ", media_ponderada)