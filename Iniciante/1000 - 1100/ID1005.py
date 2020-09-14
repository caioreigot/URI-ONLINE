a = float(input())
b = float(input())

# "MEDIA = NUMERO"
# 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade

# 'a' tem peso de 3.5 e 'b' de 7.5, os dois somados dão 11
media = ((a * 3.5) + (b * 7.5)) / 11
print("MEDIA = " + format(media, ".5f"), end='\n')