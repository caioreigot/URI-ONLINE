temp = input()
entrada = []
entrada = temp.strip('').split(' ')

codigo = int(entrada[0])
quantidade = int(entrada[1])

# dicionario com codigo/preço, respectivamente
tabela = [(1, 4.00), (2, 4.50), (3, 5.00), (4, 2.00), (5, 1.50)]
# Ex: para acessar o preço do segundo codigo, usar tabela[1][1]

# [codigo - 1] pois queremos que a lista comece pelo 1, não pelo 0
valor = tabela[codigo - 1][1]
valor = valor * quantidade

print("Total: R$ " + format(valor, ".2f"))