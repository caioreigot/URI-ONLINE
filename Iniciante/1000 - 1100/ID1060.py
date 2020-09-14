positivo = 0

for i in range(1, 7):
    numero = float(input())
    if numero > 0:
        positivo += 1

print('{} valores positivos'.format(positivo))