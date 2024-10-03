import numpy as np
import matplotlib.pyplot as plt
from random import choice, randrange, randint
from math import *
"""
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
numero_sorteado = choice(lista)
print(numero_sorteado)
numero_sorteado = randrange(100)
print(numero_sorteado)
numero = int(input("digite um numero: "))
expoente = int(input("digite um expoente: "))
resultado = pow(numero, expoente)
print(resultado)

qtd_participantes = int(input("Digite a quantidade de participantes"))
print(randint(1, qtd_participantes))
"""
nome = input("Digite seu nome para gerar um token: ")
while (True):
    token = randrange(1000, 9999)
    if token % 2 == 0:
        print(f'Olá, {nome}, o seu token é {token}! Seja bem-vindo')
        break
    else:
        continue
    
    