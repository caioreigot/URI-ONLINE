temp = input()
entrada = []
entrada = temp.strip('').split(' ')

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

if A <= 0:
    print("Impossivel calcular")
    exit()
if B <= 0:
    print("Impossivel calcular")
    exit()
if C <= 0:
    print("Impossivel calcular")
    exit()
else:
    # delta = B ** 2 - 4 * A * C
    # x1 = (- B + delta / 0.5) / 2 * A
    # x2 = (- B - delta / 0.5) / 2 * A
    delta = (B * B) - (4 * A * C)
    if delta < 0 or A == 0:
        print("Impossivel calcular")
        exit()
    else:
        x1 = (- B + delta ** 0.5) / (2 * A)
        x2 = (- B - delta ** 0.5) / (2 *  A)
        print("R1 = {:.5f}".format(x1))
        print("R2 = {:.5f}".format(x2))