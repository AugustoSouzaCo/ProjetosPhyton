"""
nome = input("Digite seu nome : ")
print('Nome do aluno: %s' %(nome))
print('Nome do aluno é {}' .format(nome))
print(f'Nome do aluno: {nome}')
"""
# print('Quantidade\tQualidade\n5 amostras\tAlta\n3 amostras\tBaixa')
# tabulação e quebra de linha
# para imprimir uma única barra invertida usa-se \\. \" para imprimir 
# aspas duplas. Desnecessario se a str foi criada com uma só aspa
'''
qtd_coloniaA = 4
qtd_coloniaB = 10
dias = 0
while qtd_coloniaB>qtd_coloniaA:
    qtd_coloniaA *= 1.03
    qtd_coloniaB *= 1.015
    dias += 1
print(f"A colonia A chegou em B em {dias} dias")
'''

'''
numero = int(input("Digite um número: "))
operador = 1
while (operador <= 10):
    resultado = numero * operador
    print(resultado)
    operador += 1
'''
'''
misturas = ['Tintas: vermelho, azul e amarelo',
            'Verde: mistura de azul e amarelo',
            'Laranja: mistura de vermelho e amarelo',
            'Roxo: mistura de vermelho e azul']
unificador = '. '
string_misturas = unificador.join(misturas)
print(string_misturas)
'''
#Dicionários; pares chave(bool,str,int...) : valor. são delimitados por {}
'''
dicionario = {'atributo' : 3,
              'atributo2': 4
              }
print(dicionario)
'''
# para acessar um valor dicionario[chave]; é possivel atribuir novos valores(atualizar)
# para criar novas chave dicionario[novaChave] = valorNovaChave
# Métodos de consulta
'''
.items() retorna uma lista de pares chave valor do dict
.keys() retorna uma lista das chaves do dict; .values() retorna os valores
'''
# leitura de valores com for de um dict
'''
for chaves in dict.keys():
    print(dict[chaves])
for valores in dict.values():
    print(valores)
for chaves, valores in dict.items():
    print(chaves, valores)
'''
# varios valores associados a uma chave
'''
loja = {'nomes': ['televisão', 'celular', 'notebook', 'geladeira', 'fogão'],
        'precos': [2000, 1500, 3500, 4000, 1500]}
'''
# acessando os valores
'''
for chave, elementos in loja.items():
  print(f'Chave: {chave}\nElementos:')
  for dado in elementos:
    print(f'\t\t{dado}')
'''
# Funções built-in
'''
.sum() somar elementos de uma estrutura de dados
.help(metodo) acessa a documentação de funções, métodos ...
.dir() exibir uma lista de atributos e metodos associados a um elemento;
lista = []
ex: dir(lista)
'''