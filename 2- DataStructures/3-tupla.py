# tupla é parecida com a lista, mas mais restrita. 
# Principal diferença:
# Tuplas são estruturas IMUTÁVEIS - classe tuple ou usando parenteses
# Listas são MUTÁVEIS - classe list ou usando colchetes

# boa prática declarar tupla com vírgula no final para evitar confusão do interpretador
frutas = ("laranja", "uva", "pera",) 

letras = tuple("Python")
numeros = tuple([1,2,3,4])

pais = ("Brasil",)

# acessar valores
print(frutas[1])

# índices negativos
print(frutas[-1])

# representação de tupla bidimensional
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6,5,"c"),
)

print(matriz[0])        # (1, "a", 2)
print(matriz[0][0])     # 1
print(matriz[0][-1])    # 2
print(matriz[-1][-1])   # "c"

carro = ("gol",)
print(isinstance(carro,tuple))
