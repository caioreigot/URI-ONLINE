nome = input()
salariofixo = float(input())
vendas = float(input())

salario = (vendas * 0.15) + salariofixo

print("TOTAL = R$ " + format(salario, ".2f"))