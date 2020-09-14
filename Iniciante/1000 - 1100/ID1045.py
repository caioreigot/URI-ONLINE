entrada = input().strip('').split(' ')

entrada.sort(key = float, reverse = True)

a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

if a >= (b + c):
    print("NAO FORMA TRIANGULO")

else:

    if (a ** 2) == (b ** 2) + (c ** 2):
        print("TRIANGULO RETANGULO")

    if (a ** 2) > ((b ** 2) + (c ** 2)):
        print("TRIANGULO OBTUSANGULO")

    if (a ** 2) < ((b ** 2) + (c ** 2)):
        print("TRIANGULO ACUTANGULO")

    if a == b and a == c and b == a and b == c and c == a and c == b:
        print("TRIANGULO EQUILATERO")

    if (a == b or a == c or b == a or b == c or c == a or c == b) and (a != b or a != c or b != a or b != c or c != a or c != b):
        print("TRIANGULO ISOSCELES")
