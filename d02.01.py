# importando sem  aliasimport matplotlib
# importando com alias import 
import matplotlib.pyplot as plt
# importando uma função específica de uma lib; não precisa especificar a lib
from random import choice
# importando todos os metodos de uma bibioteca; dessa forma não é necessario
# usar o nome dela para chamar um método
# from math import *;
estudantes = ["João", "Maria", "José", "Ana"]
notas = [8.5, 9, 6.5, 7]
'''
plt.bar(x = estudantes, height = notas)
plt.show()
'''
estudante = choice(estudantes)
print(estudante)

