# Aula 20 Funções

print("Valor da variável name - __main__ | ", __name__)

def mensagem ():
    print("Execução da função mensagem")

def mensagem_com_parametros(texto= ""):
    texto = input("Digite o texto a ser exibido: ")
    print("Mensagem: ", texto)

def calculo_imc(peso, altura):
    return "O cálculo do imc é: ", peso / altura ** 2



if (__name__== "__main__"):
    mensagem()
    mensagem_com_parametros()
    print(calculo_imc(100, 1.75))