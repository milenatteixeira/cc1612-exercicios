clas = float(input("digite a classificação do funcionário: "))

if clas == 0.0:
    print("Classificação %.2f = inaceitável." % clas)
elif clas == 0.4:
    print("Classificação %.2f = aceitável." % clas)
elif clas >= 0.6:
    aumento = clas * 2400
    print("Classificação %.2f = excelente." % clas)
    print("O valor do aumento é %.2f" % aumento)
else:
    print("Uma classificação inválida foi inserida. Tente novamente.")