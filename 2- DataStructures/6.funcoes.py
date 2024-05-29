def exibir_mensagem():
    print("Olá mundo")

def exibir_mensagem2(nome):
    print(f"Olá, {nome}!")

def exibir_mensagem3(nome="Anônimo"):
    print(f"Olá, {nome}!")

exibir_mensagem()
exibir_mensagem2("Johnny")
exibir_mensagem3()
exibir_mensagem3(nome="Johnson")


# python pode retornar mais de um valor ao fim da função

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero-1
    sucessor = numero+1
    return antecessor,sucessor

print(calcular_total([10,20,34,50]))
print(retorna_antecessor_e_sucessor(10))


# OBS: uma função sempre retorna None por padrão!

def salvar_carro(marca,modelo,ano,placa):
    print(f"Carro salvo com sucesso!")
    print(f"Marca: {marca}, Modelo: {modelo}, Ano: {ano}, Placa: {marca}.")

# argumentos em função - forma 1
salvar_carro("Fiat","Palio",1999,"ABC-1234")

# argumentos em função - forma 2
salvar_carro(marca="Fiat",modelo="Palio",ano=1999,placa="ABC-1234")

# argumentos em função - forma 3 (passando dict [kwargs])
salvar_carro(**{"marca":"Fiat","modelo":"Palio","ano":1999,"placa":"ABC-1234"})


# Exemplo de uso de args e kwargs

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    metadata = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{metadata}"
    print(mensagem)

exibir_poema("Terça-feira, 28 de Maio de 2024", # data_extenso
             "Zen of Python", # *args
             "Beautiful is better than ugly.", # *args
             autor="Tim Peters", # **kwargs
               ano=1999) # **kwargs


# PARÂMETROS ESPECIAIS DA FUNÇÃO

# Por padrão, argumentos podem ser passados em uma função por posição ou explicitamente pelo nome.
# Para melhorar a legibilidade, faz sentido restringir a maneira pela qual argumentos possam ser passados
# Deste modo, o desenvolvedor olha a definição da função e já sabe se os itens são passados por:

# 1- POSIÇÃO (padrão)
# 2- APENAS POSIÇÃO OU APENAS NOME (/)
# 3- NOME (*)

# --> def funcao(pos1, pos2, /, pos_ou_kwd, *, kwd1,kwd2)

# Ou seja, com "/" e "*", se restringe como devem ser passados os argumentos.

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel,*, cor,valor):
    print(modelo, ano, placa, marca, motor, combustivel,cor,valor)

# POSIÇÃO, KWARGS, KWARGS
criar_carro("Palio",1999,"ABC-1234", marca="Fiat", motor="1.0",combustivel="gasolina",cor="preto",valor=90000)
# POSIÇÃO, POSIÇÃO, KWARGS
criar_carro("Palio",1999,"ABC-1234", "Fiat","1.0","gasolina",cor="preto",valor=90000)


# OBJETOS DE PRIMEIRA CLASSE

# Em Python, tudo é objeto; logo, funções também são objetos.
# Com isso, é possível:
# 1- atribuir funções a variáveis
# 2- passar funções como parâmetros de funções
# 3- usar funções como valores em estruturas de dados (listas, tuplas, dicts, etc)
# 4- usar uma função como valor de retorno pra outra função (closure)

# Ser capaz de fazer tudo isso é o que torna funções objetos de primeira classe.

def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def exibir_resultado(a,b,operacao):
    resultado = operacao(a,b)
    print(f"O resultado da operação de {operacao.__name__} escolhida a ser realizada entre {a} e {b} é = {resultado}.")

exibir_resultado(3,2,multiplicar)

op = subtrair

print(op(6,3))



# ESCOPO GLOBAL E LOCAL

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))