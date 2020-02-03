def doacao(sexo, peso):
    if sexo == "feminino":
        if peso >=50:
            print("Apta para doar.")
        else:
            print("Não apta para doar.")
    elif sexo == "masculino":
        if peso >=60:
            print("Apto para doar.")
        else:
            print("Não apto para doar.")
    
