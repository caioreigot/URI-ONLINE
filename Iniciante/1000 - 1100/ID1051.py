salario = float(input())

if salario >= 0.00 and salario <= 2000.00:
    print('Isento')

if salario > 2000.00 and salario <= 3000.00:
    aDividir = (salario - 2000.00)
    imposto = aDividir * 0.08
    print('R$ {:.2f}'.format(imposto))

if salario > 3000.00 and salario <= 4500.00:
    # imposto do valor entre 2k a 3k (8%)
    imposto8porcent = 1000.00 * 0.08
    # imposto do valor entre 3k e 4500 (18%)
    imposto18porcent = (salario - 3000.00) * 0.18
    impostototal = imposto8porcent + imposto18porcent
    print('R$ {:.2f}'.format(impostototal))

if salario > 4500.00:
    # imposto do valor entre 2k a 3k (8%)
    imposto8porcent = 1000.00 * 0.08
    # imposto do valor entre 3k e 4500 (18%)
    imposto18porcent = 1500.00 * 0.18
    # imposto do valor > 4500
    imposto28porcent = (salario - 4500.00) * 0.28
    impostototal = imposto8porcent + imposto18porcent + imposto28porcent
    print('R$ {:.2f}'.format(impostototal))
