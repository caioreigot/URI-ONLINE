temp = input()
entrada = []
entrada = temp.strip('').split(' ')
n1 = float(entrada[0])
n2 = float(entrada[1])
n3 = float(entrada[2])
n4 = float(entrada[3])

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print('Media: {:.1f}'.format(media))
if media >= 7.0:
    print("Aluno aprovado.")
if media < 5.0:
    print("Aluno reprovado.")
if media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    nota = float(input())
    notaexame = (media + nota) / 2
    print("Nota do exame: {}".format(nota))
    if notaexame >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    mediafinal = notaexame
    print("Media final: {}".format(mediafinal))