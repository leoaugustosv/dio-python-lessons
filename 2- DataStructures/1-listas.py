# declarar lista com valores
frutas = ["laranja","uva","maca"]
print(frutas)

# declarar lista vazia
frutas = []
print(frutas)

# declarar lista usando construtor list (que pede argumento iteravel)
letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

# declarando lista com tipos diferentes
carro = ["Ferrari","F8",4200000,2020,2900,"São Paulo", True]
print(carro)
print(carro[1])
print(carro[2])

# index negativo começa do fim
print(carro[-2]) 
print(carro[-3])


# representação de lista bidimensional
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6,5,"c"],
]

print(matriz[0])        # [1, "a", 2]
print(matriz[0][0])     # 1
print(matriz[0][-1])    # 2
print(matriz[-1][-1])   # "c"

# fatiamento (slice) de listas: [inicio:fim:step]
fatiar = list("python")

print(fatiar[2:])       # ["t","h","o","n"]
print(fatiar[:2])       # ["p","y"]
print(fatiar[1:3])      # ["y","t"]
print(fatiar[0:3:2])    # ["p","t"]
print(fatiar[::])       # ["p","y",t","h","o","n"]
print(fatiar[::-1])     # ["n","o","h","t","y","p"]

# acessar dados com for
for c in carro:
    print(c)

# usando enumerate para exibir índices
for i,c in enumerate(carro):
    print(f"{i}: {c}")



# acrescentando valores em uma lista já existente - VERSÃO 1
numeros = [1, 4, 90, 13,46,93,20, 14,53,78]
pares = []

for n in numeros:
    if n%2==0:
        pares.append(n)


quadrado = []
for n in numeros:
    quadrado.append(n**2)

# acrescentando valores em uma lista já existente - VERSÃO 2 (comprehension)
numeros2 = [1, 4, 90, 13,46,93,20, 14,53,78]
pares2 = [n for n in numeros2 if n % 2 == 0]

quadrado2 = [n**2 for n in numeros2 ]
print(quadrado)
print(quadrado2)


