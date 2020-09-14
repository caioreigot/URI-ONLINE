temp = input()
entrada = temp.strip('').split(' ')

A, B, C = int(entrada[0]), int(entrada[1]), int(entrada[2])

def simpleSort(a, b, c):
    numeros = [A, B, C]
    numeros.sort()
    print(numeros[0])
    print(numeros[1])
    print(numeros[2])
    print("")
    
simpleSort(A, B, C)

print(A)
print(B)
print(C)