# o veiculo faz 12 KM/L
tempo = int(input())
velmedia = int(input())
# distancia é igual a tempo vezes velocidade
distancia = (tempo * velmedia)
# gasto é igual a distancia dividido pelo consumo de KM/L
gasto = (distancia / 12)

print("{:.3f}".format(gasto))

