numero = int(input())
horas = int(input())
dinheiroporhora = float(input())

salario = float(dinheiroporhora * horas)

print("NUMBER = " + format(numero))
print("SALARY = U$ " + format(salario, ".2f"))