nome = "Leonardo Augusto"

#Valor na posição do iterável
print(nome[0])

#Antes dos dois pontos: onde começar (start) // depois dos dois pontos: onde parar (stop)
print(nome[3:8])

#Sem especificar em um dos lados, não limita o inicio ou o fim
print(nome[:5])
print(nome[5:])

#Vazio dos dois lados: traz todos os valores
print(nome[:])

#Depois do segundo ponto: de quantos itens em quantos itens (step)
print(nome[0:12:2])
print(nome[0:16:3])

#Espelhamento de string: sem start, sem stop, e o step -1
print(nome[::-1])