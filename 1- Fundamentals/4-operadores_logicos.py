saldo = 1000
saque = 200
limite = 100

# e
print(saldo >= saque and saque <= limite)

# ou
print(saldo >= saque or saque <= limite)

#negacao
print(not (saldo >= saque and saque <= limite))
print(not (saldo >= saque or saque <= limite))