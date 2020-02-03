ano = int(input("digite o ano:"))
anoDigitado = ano
# de acordo com o horóscopo chinês, os animais são listados de 1 a 12, começando pelo rato.
ano = ano - 4
ano = ano % 12
ano = ano + 1

if anoDigitado < 0:
    print("Ano inválido.")
else:
    if ano == 1:
        print("O ano %d é o ano do rato." % anoDigitado)
    elif ano == 2:
        print("O ano %d é o ano do boi." % anoDigitado)
    elif ano == 3:
        print("O ano %d é o ano do tigre." % anoDigitado)
    elif ano == 4:
        print("O ano %d é o ano da lebre." % anoDigitado)
    elif ano == 5:
        print("O ano %d é o ano do dragão." % anoDigitado)
    elif ano == 6:
        print("O ano %d é o ano da cobra." % anoDigitado)
    elif ano == 7:
        print("O ano %d é o ano do cavalo." % anoDigitado)
    elif ano == 8:
        print("O ano %d é o ano do carneiro." % anoDigitado)
    elif ano == 9:
        print("O ano %d é o ano do macaco." % anoDigitado)
    elif ano == 10:
        print("O ano %d é o ano do galo." % anoDigitado)
    elif ano == 11:
        print("O ano %d é o ano do cachorro." % anoDigitado)
    elif ano == 12:
        print("O ano %d é o ano do porco." % anoDigitado)
    else:
        print("Um problema foi encontrado, esse valor de signo não existe no calendário chinês.")