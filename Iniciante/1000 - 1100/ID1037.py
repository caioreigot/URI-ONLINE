numero = float(input())

if numero >= 0 and numero <= 25:
    print("Intervalo [0,25]")

elif numero > 25 and numero <= 50:
    print("Intervalo (25,50]")

elif numero >= 75 and numero <= 100:
    print("Intervalo [75,100]" if numero == 75 else "Intervalo (75,100]")

else:
    print("Fora de intervalo")