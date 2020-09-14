# Faça um programa que calcule e mostre o volume de uma esfera sendo 
# fornecido o valor de seu raio (R). 

R = float(input())
pi = 3.14159
formula = (4/3) * pi * R ** 3

print("VOLUME = " + format(formula, ".3f"))
