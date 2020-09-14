entrada = input().strip('').split(' ')

tempo1 = int(entrada[0])
tempo2 = int(entrada[1])

count = 0

if tempo1 == tempo2:
    print("O JOGO DUROU 24 HORA(S)")
else:
    while tempo1 != tempo2:
        tempo1 += 1
        count += 1
        if tempo1 >= 24:
            tempo1 = 0

    print("O JOGO DUROU {} HORA(S)".format(count))
