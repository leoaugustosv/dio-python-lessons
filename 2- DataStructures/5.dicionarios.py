# dicionário é um conjunto não-ordenado de pares "chave:valor", onde as chaves são únicas para cada instância.
# Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor, separada por vírgulas.
# Chaves são únicas.

# formas de criar um dicionário
pessoa = dict(nome="Leonardo",idade=22)
pessoa = {"nome":"Leonardo","idade":22,"chave":"valor"}
pessoas = pessoa.copy()


# adicionar uma nova chave em dicionário
pessoa["telefone"] = "3333-0000"


# acessando o valor da chave especificada
print(pessoa["telefone"])

# sobrescrevendo valor de uma chave
pessoa["chave"] = "sobrescrita"

# estruturas aninhadas
contatos = {
    "leo@leo.com.br":{"nome":"Leonardo","idade":22,"telefone":"3333-0000"},
    "mauro@mauro.com.br":{"nome":"Mauro","idade":41,"telefone":"96987-2000"},
}

# acessar valor de uma chave em um dicionario aninhado
print(contatos["leo@leo.com.br"]["idade"])


#iterar dicionários - forma 1
for c in contatos:
    print(c,contatos[c])

print("="*50)

#iterar dicionários - forma 2 (mais declarativa)
for chave, valor in contatos.items():
    print(chave,valor)

print("="*100)
################ MÉTODOS #################


# [].copy - cria uma copia do dicionario
backup_contatos = contatos.copy()
novos_contatos = contatos.copy()

print(backup_contatos)
backup_contatos["leo@leo.com.br"]["nome"] = "Leo"
print(backup_contatos)

# dict.fromkeys - cria chaves com um valor especificado (se não especificado, valor é NONE)
novos_contatos.clear()
novos_contatos = dict.fromkeys(["nome","telefone"])
print(novos_contatos)

# [].get - outra forma de acessar valor em um dicionario

novos_contatos["telefone"] # gera exception caso chave nao exista
novos_contatos.get("telefone") # não gera exception caso chave nao exista (retorna None)

novos_contatos.get("chave",{}) # caso não exista a chave, retorna o valor especificado


# [].items - retorna uma lista de tuplas (útil para iterar sobre valores de um dict)
novos_contatos.items()

# [].keys - retorna apenas as chaves de um dicionario
contatos_finais = novos_contatos.copy()
contatos_finais.keys()

# [].pop - remove uma chave especificada do dicionário e retorna o valor encontrado pra remoção
# caso não exista a chave, retorna exception, ou se um segundo argumento for dado, retorna esse segundo argumento

contatos_finais = {"leo@leo.com.br":{"cidade":"São Paulo","time":"corinthians"},"mauro@mauro.com.br":{"cidade":"Manaus","time":"amazonense"}}
print(contatos_finais)
print(contatos_finais.pop("mauro@mauro.com.br","não encontrado"))

# [].popitem - remove e retorna o último item (chave:valor) de um dicionário
print(contatos_finais.popitem())
print("="*100)

# [].setdefault - se a chave NÃO EXISTIR no dicionario, adiciona com o valor especificado.
# se a chave EXISTIR, retorna o valor que já existe, sem alterar
pessoas.setdefault("esposa","Bianca")
print(pessoas)

# [].update - insere um item (chave:valor) no dicionario
contatos_finais.update({"leo@leo.com.br":{"nome":"Leo","idade":22}})
contatos_finais.update({"bianca@bianca.com.br":{"nome":"Bianca","idade":25}})
contatos_finais.update(pessoa)
print("Chaves: ",contatos_finais.keys())

# [].keys - retorna todos os valores de um dicionario
print("Valores: ",contatos_finais.values())

# [] in - retorna verdadeiro se um valor é uma chave dentro de um dicionario
print("chave" in contatos_finais)
print("chave" in contatos_finais["leo@leo.com.br"])

# [].del - remove uma chave do dicionario, não retornando nada
del contatos_finais["bianca@bianca.com.br"]["idade"]
del contatos_finais["bianca@bianca.com.br"]
del contatos_finais # apaga o dicionario todo!
print(contatos_finais)
