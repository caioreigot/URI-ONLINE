qntPositivos = 0
arrayPositivos = []

for i in range (6):
    valor = float(input())
    if (valor > 0):
        qntPositivos += 1
        arrayPositivos.append(valor)

print('{} valores positivos'.format(qntPositivos))

somaPositivos = 0
for positivo in arrayPositivos:
    somaPositivos += positivo

mediaPositivos = somaPositivos / len(arrayPositivos)
print("{0:.1f}".format(mediaPositivos))