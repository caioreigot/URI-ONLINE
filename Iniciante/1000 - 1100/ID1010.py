# 12 1 5.30 <-- Código da peça, unidades, preço
# 16 2 5.10 <-- Código da peça, unidades, preço
# Valor a pagar: 15.50

temp = input()
temp2 = input()

entrada1 = []
entrada1 = temp.strip('').split(' ')

unidades1 = int(entrada1[1])
valorunidade1 = float(entrada1[2])

entrada2 = []
entrada2 = temp2.strip('').split(' ')

unidades2 = int(entrada2[1])
valorunidade2 = float(entrada2[2])

total = ((valorunidade1 * unidades1) + (valorunidade2 * unidades2))

print("VALOR A PAGAR: R$ " + format(total, ".2f"), end="\n")






