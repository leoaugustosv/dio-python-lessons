# [].append - adicionar elemento

lista = []

lista.append(1)
lista.append("Python")
lista.append("Java")
lista.append([1,40,30,20])
lista.append(5)
lista.append(10)
lista.append(15)

# [].copy - retorna uma lista idêntica, mas com uma instância diferente para evitar alterações na lista original

l2 = lista.copy()
l3 = lista.copy()

# [].clear - limpar lista

lista.clear()

# [].count - contar quantidade de vezes que um elemento aparece na lista

l2.count("Python") # 1

# [].extend - fundir com outro iterável, incluindo valores duplicados

l2.extend(l3)
print(l2)

# [].index - retorna o primeiro índice em que o objeto passado pode ser encontrado

l3.index("Java") # 2

# [].pop - retorna e remove o ultimo elemento da lista (comportamento de pilha) - também é possível passar o indice

print(l3.pop())
print(l3)
l3.pop(0) # 1

# [].remove - remove a primeira ocorrência do objeto passado

l3.remove("Python")

# [].reverse - inverte a ordem da lista

l3.reverse()

# [].sort - ordena a lista

l2.sort() # ordenação padrao em ordem descendente
l2.sort(reverse=True) # espelha/inverte a ordenação
l2.sort(key=lambda x: len(x)) # key=ordenação customizada - ex: ordenando de acordo com o tamanho da string
l2.sort(key=lambda x: len(x), reverse=True)

# len([]) - tamanho de um objeto (lista: quantidade de elementos dentro)

len(l2)


# sorted([]) - função built-in de Python pra ordenação

sorted(l3)
sorted(l3,key=lambda x: len(x), reverse=True)


