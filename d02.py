# Sets; Estrutura de dados built-in do python; é uma coleção não ordenada
# Não são ordenados portanto não é certo que vão aparecer na ordem que
# está declarada; não é possivel acessar com a notação de []
# Não permite duplicatas
# Se transformar uma lista com duplicatas em um Set elas não serão captadas
# Pode ser criada com elementos de tipos diferentes
# é possivel passar listas como argumento da função set para converte-la
'''
carros = {'Jetta Variant', 'Passat', 'Crossfox', 'Dodge Jorney'}
for carro in carros:
    print(carro)
'''
# Função para verificar disjunção de conjuntos (excludentes); retorna bool
'''
set.isdisjoint()
'''
# Interssecção usa-se o & entre os Sets ou
'''
set.intersection()
'''
# União usa-se uma única barra vertical | ou; é possível adicionar novos elementos tb
'''
set.union()
'''
# Operador in para verificar se um valor está no Set; retorna um bool
'''
print('Crossfox' in carros)
'''