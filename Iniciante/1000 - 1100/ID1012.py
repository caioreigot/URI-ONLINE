# armazenei o input em uma variavel temporária
temp = input()
# iniciei uma lista chamada "entrada"
entrada = []
# adicionei a lista a variável temp, sendo cada elemento entre os espaços um item
entrada = temp.strip('').split(' ')

# agora eu atribuo o A, B, C pegando um por um na lista em seus lugares "[]"
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

# as fórmulas pra calcular cada área estão na internet, a variavel que vai ser a base/altura está especificado no urionline
print("TRIANGULO: " + format((A * C) / 2, ".3f"))
print("CIRCULO: " + format(3.14159 * (C ** 2), ".3f"))
print("TRAPEZIO: " + format((B + A) * C / 2, ".3f"))
print("QUADRADO: " + format(B * B, ".3f"))
print("RETANGULO: " + format(A * B, ".3f"))
