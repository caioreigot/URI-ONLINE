temp = input()
entrada = []
entrada = temp.strip('').split(' ')

x1 = float(entrada[0])
y1 = float(entrada[1])

temp2 = input()
entrada2 = []
entrada2 = temp2.strip('').split(' ')

x2 = float(entrada2[0])
y2 = float(entrada2[1])

# dividindo cada parte da função
primeiraparte = (x2 - x1) ** 2
segundaparte = (y2 - y1) ** 2
terceiraparte = primeiraparte + segundaparte
# por fim, fazendo a raiz
ultimaparte = terceiraparte ** 0.5

print('{:.4f}'.format(ultimaparte), end="\n")

