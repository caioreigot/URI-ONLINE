entrada = input().strip('').split(' ')

a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

if a + b > c:
    if b + c > a:
        if a + c > b:
            print("Perimetro = {}".format(a + b + c))

if a + b <= c or b + c <= a or a + c <= b:
    ordemcrescente = [a, b , c]
    ordemcrescente.sort(reverse = True)
    areatrapezio = ((ordemcrescente[0] + ordemcrescente[1]) * c) / 2
    print("Area = {}".format(areatrapezio))

