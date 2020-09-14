# entrada: hora e minuto
# ex: 7 8 9 10 (7h 8m até 9h 10m)

entrada = input().strip('').split(' ')

hora1 = int(entrada[0])
minuto1 = int(entrada[1])

hora2 = int(entrada[2])
minuto2 = int(entrada[3])

horas = 0
minutos = 0

if hora1 == hora2 and minuto1 == minuto2:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if hora1 != hora2 and minuto1 == minuto2:
        while hora1 != hora2:
            hora1 += 1
            horas += 1
            if hora1 >= 24:
                hora1 = 0
    else:
        # TODO

    print("O JOGO DUROU {} HORA(S) e {} MINUTO(S)".format(horas, minutos))
