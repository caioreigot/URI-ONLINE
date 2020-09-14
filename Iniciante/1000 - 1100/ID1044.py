entrada = input().strip('').split(' ')

entrada.sort(key=int)

a = int(entrada[0])
b = int(entrada[1])

if b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

