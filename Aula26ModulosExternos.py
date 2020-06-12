# Aula 26 Módulos Externos
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [1500,1800,2100,1900,1900,2000]

legenda = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']

plt.xticks(x, legenda)

plt.plot(x, y)
plt.show()



