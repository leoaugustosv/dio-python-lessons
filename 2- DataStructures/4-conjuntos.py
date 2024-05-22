# conjuntos = set
# set é uma coleção que não possui objetos repetidos
# normalmente usados pra representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.

# set não garante a ordem em que os valores foram inseridos!!!

exemploSet = {1,2,3,4,5,6}

numeros = set([1,1,2,3,4,4,5,1,3,4])
print(numeros)

abacaxi = set("abacaxi")
print(abacaxi)

carros = set(("gol","palio","fusca","gol","fusca"))
print(carros)

# acessar dados de um set: necessário converter o set para uma lista
carros2 = list(carros)
print(carros2[0])



##### FUNÇÕES

# set{}.add - adicionar um elemento a um conjunto
sorteio = {1,23,3,4,8485,465,265,25,1,5,4,6,8}
sorteio.add(3)
sorteio.add(23)

# set{}.copy - criar uma cópia do set
sorteio2 = sorteio.copy()
print(sorteio2)

# set{}.remove - descarta um valor dentro do set (caso o valor não exista, retorna exception)
sorteio2.remove(5)

# set{}.discard - descarta um valor dentro do set (caso o valor não exista, não retorna exception)
sorteio2.discard(4)

# set{}.pop - retorna e remove o primeiro valor do set (comportamento de fila)

print(sorteio2.pop())
print(sorteio2)

# operador in - auxilia na verificação se um valor está dentro do set
print(465 in sorteio)

# set{}.union - unir conjuntos/sets

setA = {1,2}
setB = {3,4}

print(setA.union(setB))

# set{}.intersection - retornar valores iguais entre conjuntos
setA = {1,2,4,5}
setB = {3,4,2}
print(setA.intersection(setB))

# set{}.difference - retornar valores que estão neste set e não estão no set do argumento
setA = {1,2,3}
setB = {2,3,4}
print(setA.difference(setB))
print(setB.difference(setA))

# set{}.symmetric_difference - retornar valores que não são iguais entre conjuntos
setA = {1,2,4,5}
setB = {3,4,2}
print(setA.symmetric_difference(setB))

# set{}.issubset - retorna true apenas se todos os elementos deste set estão dentro do set do argumento
setA = {1,2,3}
setB = {4,1,2,5,6,3}
print(setA.issubset(setB))

# set{}.issuperset - retorna true apenas se todos os elementos do set do argumento estão dentro deste set
setA = {1,2,3}
setB = {4,1,2,5,6,3}
print(setA.issuperset(setB))

# set{}.isdisjoint - retorna true apenas se todos os elementos deste set não estão presentes no set do argumento
setA = {1,2,3,4,5}
setB = {6,7,8,9}
setC = {1,0}
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))