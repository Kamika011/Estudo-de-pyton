

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >=saque)
print(exp_2)


conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente =  (conta_especial and saldo >= saque)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)

print(True and True)   # True, porque ambas as condições são True
print(True and False)  # False, porque uma das condições é False
print(False and False) # False, porque ambas as condições são False
print(True or False)   # True, porque uma das condições é True
print(True or False)   # True, novamente porque uma das condições é True
print(False or False)  # False, porque ambas as condições são False





