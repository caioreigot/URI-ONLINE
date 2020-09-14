temp = input()

entrada = []
entrada = temp.strip('').split(' ')

A = int(entrada[0])
B = int(entrada[1])
C = int(entrada[2])

maiorab = (A + B + abs(A - B)) / 2
maiorbc = (B + C + abs(B - C)) / 2

maior = (maiorab + maiorbc + abs(maiorab - maiorbc)) / 2

print("{} eh o maior".format(int(maior)))
