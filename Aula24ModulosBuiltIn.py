# Aula 24 - Módulos Buit In
import math
import time
import random

print("********** match **********")
print(math.ceil(3.2))
print(math.floor(3.7))
print(math.fsum([1,2,3]))
print(math.sqrt(16))

print("********** time **********")
print(time.time())
print(time.localtime())
print(time.localtime().tm_hour)
print((time.clock()))

def cont_tempo():
    inicio = time.clock()
    input("Digite seu nome: ")
    fim = time.clock()
    tempo = round(fim - inicio, 2)

    print("Você levou " + str(tempo) + " segundos para digitar seu nome")

print("********** random **********")
print(random.randint(0,10))

def mega_sena():
    jogo = []
    while len(jogo) < 6:
        num = random.randint(1,60)
        if num in jogo:
            continue
        else:
            jogo.append(num)

    print("Numeros aleatórios para a mega sena: ", sorted(jogo))

if(__name__ == "__main__"):
    cont_tempo()
    mega_sena()

alunos = ["João", "Pedro", "Maria", "Helena", "Guilherme"]

print(random.choice(alunos))

print(random.sample(alunos, 3))






