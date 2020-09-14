testes = int(input())

def mdc(num1, num2):
    resto = None
    while resto is not 0:
        resto = num1 % num2
        num1  = num2
        num2  = resto

    return num1

for i in range(testes):
    temp = input()

    figurinhas = []
    figurinhas = temp.strip('').split(' ')

    a = int(figurinhas[0])
    b = int(figurinhas[1])
    
    resultado = mdc(a, b)
    print(resultado)
