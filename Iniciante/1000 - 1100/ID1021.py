# quantia = float(input()) * 1000
# notas = [100000, 50000, 20000, 10000, 5000, 2000]
# moedas = [1000, 500, 250, 100, 50, 10]
# print("NOTAS:")
# for i in notas:
#     print("{} nota(s) de R$ {}".format(int((quantia) // i), format(i / 1000, ".2f")))
#     quantia %= i
# print("MOEDAS:")
# for j in moedas:
#     print("{} moeda(s) de R$ {}".format(int(quantia // j), format(j / 1000, ".2f")))
#     quantia %= j

valor_total = float(input())

notas100 = int(valor_total // 100)
notas50 = int((valor_total - (notas100 * 100)) // 50)
# Observe o padrão: O valor menor é sempre a subtração dos anteriores dividido pelo valor dele próprio (com a operação "//")
notas20 = int(((valor_total - (notas100 * 100)) - (notas50 * 50)) // 20)
notas10 = int(((valor_total - (notas100 * 100)) - (notas50 * 50) - (notas20 * 20)) // 10)
notas5 = int(((valor_total - (notas100 * 100)) - (notas50 * 50) - (notas20 * 20) - (notas10 * 10)) // 5)
notas2 = int(((valor_total - (notas100 * 100)) - (notas50 * 50) - (notas20 * 20) - (notas10 * 10) - (notas5 * 5)) // 2)

moedas1 = int(((valor_total - (notas100 * 100)) - (notas50 * 50) - (notas20 * 20) - (notas10 * 10) - (notas5 * 5) - (notas2 * 2)) // 1)
moedas50cents = int(((valor_total - (notas100 * 100)) - (notas50 * 50) - (notas20 * 20) - (notas10 * 10) - (notas5 * 5) - (notas2 * 2) - moedas1) // 0.50)
moedas25cents = int(((valor_total - (notas100 * 100)) - (notas50 * 50) - (notas20 * 20) - (notas10 * 10) - (notas5 * 5) - (notas2 * 2) - moedas1 - (moedas50cents * 0.50)) // 0.25)
moedas10cents = int(((valor_total - (notas100 * 100)) - (notas50 * 50) - (notas20 * 20) - (notas10 * 10) - (notas5 * 5) - (notas2 * 2) - moedas1 - (moedas50cents * 0.50) - (moedas25cents * 0.25)) // 0.10)
moedas05cents = int(((valor_total - (notas100 * 100)) - (notas50 * 50) - (notas20 * 20) - (notas10 * 10) - (notas5 * 5) - (notas2 * 2) - moedas1 - (moedas50cents * 0.50) - (moedas25cents * 0.25) - (moedas10cents * 0.10)) // 0.05)
moedas01cents = int(((valor_total - (notas100 * 100)) - (notas50 * 50) - (notas20 * 20) - (notas10 * 10) - (notas5 * 5) - (notas2 * 2) - moedas1 - (moedas50cents * 0.50) - (moedas25cents * 0.25) - (moedas10cents * 0.10) - (moedas05cents * 0.05) + 0.00001) // 0.01)

# loops para passar os valores/montates das moedas que possam ser substituidas por outras maiores
while moedas05cents >= 2:
    temp = moedas05cents
    moedas10cents = temp
    moedas05cents -= 2

while moedas25cents >= 2:
    temp = moedas25cents
    moedas50cents = temp
    moedas25cents -= 2

while moedas50cents >= 2:
    temp = moedas50cents
    moedas1 = temp
    moedas50cents -= 2

while moedas1 >= 2:
    temp = moedas1
    notas2 = temp
    moedas1 -= 2

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(notas100))
print("{} nota(s) de R$ 50.00".format(notas50))
print("{} nota(s) de R$ 20.00".format(notas20))
print("{} nota(s) de R$ 10.00".format(notas10))
print("{} nota(s) de R$ 5.00".format(notas5))
print("{} nota(s) de R$ 2.00".format(notas2))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(moedas1))
print("{} moeda(s) de R$ 0.50".format(moedas50cents))
print("{} moeda(s) de R$ 0.25".format(moedas25cents))
print("{} moeda(s) de R$ 0.10".format(moedas10cents))
print("{} moeda(s) de R$ 0.05".format(moedas05cents))
print("{} moeda(s) de R$ 0.01".format(moedas01cents))