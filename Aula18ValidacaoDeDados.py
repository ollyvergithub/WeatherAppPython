# Aula 18 Validação de Dados

repetir = 's'
fatura = []
total = 0
valid_preco = False

while repetir == 's':
    produto = input('Digite o nome do produto: ')

    while valid_preco == False:
        try:
            preco = input('Digite o preço do produto: ')
            preco = float(preco)
            if preco <= 0:
                print("O preço precisa ser mairo que 0")
            else:
                valid_preco = True
        except:
            print("Digite um valor válido, separado por (.)")

    fatura.append([produto,preco])
    total += preco
    valid_preco = False
    repetir = input('Deseja comprar mais algum produto? (S ou N) ').lower()

for i in fatura:
    print(i[0],'-',i[1])

print('O total da fatura é:',total)
