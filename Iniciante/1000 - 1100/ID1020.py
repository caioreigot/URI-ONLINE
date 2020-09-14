dias_vividos = int(input())

anos = dias_vividos // 365
meses = (dias_vividos - (anos * 365)) // 30
dias = (dias_vividos - (anos * 365)) - (meses * 30)

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))