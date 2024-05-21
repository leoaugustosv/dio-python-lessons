nome = "Leo"
idade = 19
profissao = "Programador"
linguagem = "Python"
PI = 3.14159

# Forma 1: % (antiga)
print("Oi, sou o %s. Tenho %d anos, trabalho como %s e estou aprendendo %s." % (nome, idade, profissao, linguagem))

# Forma 2: format
print("Oi, sou o {}. Tenho {} anos, trabalho como {} e estou aprendendo {}.".format(nome, idade, profissao, linguagem))
print("Oi, sou o {3}. Tenho {2} anos, trabalho como {1} e estou aprendendo {0}.".format(linguagem,profissao,idade,nome))

# Forma 3: fstring
print(f"Oi, sou o {nome}. Tenho {idade} anos, trabalho como {profissao} e estou aprendendo {linguagem}.")
print(f"O valor de PI é: {PI:.2f}")
print(f"O valor de PI é: {PI:10.2f}") #espaços em branco
