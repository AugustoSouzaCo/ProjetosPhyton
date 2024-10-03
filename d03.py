from random import randint

notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]
nomes = []
notas_juntas = []
notas_separadas = []

for item in notas_turma:
    if type(item) == str:
        nomes.append(item)
    else: 
        notas_juntas.append(item)

for i in range(0, len(notas_juntas), 3):
    notas_separadas.append([notas_juntas[i], notas_juntas[i+1], notas_juntas[i+2]])

# List comprehension variavel = [expressão for item in list]

def getmedia(lista):
   calculo = sum(lista) / len(lista)
   return calculo

medias = [round( getmedia(notas), 1) for notas in notas_separadas]

nomes = [('João', 'J523'), ('Maria', 'M482'), ('José', 'J643'), ('Cláudia', 'C23'), ('Ana', 
'A755')]
nome_media = [nome[0] for nome in nomes]

# Built-in function zip; parear medias e nomes
estudantes = list(zip(nome_media, medias))
candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 6]
# para desparear usar *
nome, media = zip(*estudantes)
nome = list(estudantes)
media = list(estudantes)

# desempacotar tuplas em variáveis
cadastro = ("Júlia", 23, "São Paulo", "SP", "Python para DS 1")
nome, idade, cidade, estado, turma = cadastro


estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]
'''
def gera_codigo(lista):
  for estudante in lista:
    estudante.split()
    estudante[0] + str(randint(0,999))
'''
def gera_codigo():
  return str(randint(0,999))

codigo_estudante = []

for i in range(len(estudantes)):
  codigo_estudante.append((estudantes[i], estudantes[i][0] + gera_codigo()))


