def f1(senha):
    if len(senha)>=8:
        return True
    else:
        return False   
def f2(senha):
    ctrl=0
    for x in senha:
        if x.isupper() == True:
          ctrl=1
    if ctrl == 1:
        return True
    else:
        return False    
def f3(senha):
    ctrl=0
    for x in senha:
        if x.islower() == True:
          ctrl=1
    if ctrl == 1:
        return True
    else:
        return False 
    
def f4(senha):
    ctrl=0
    for x in senha:
        if x.isdigit() == True:
          ctrl=1
    if ctrl == 1:
        return True
    else:
        return False
def confirm(senha):
    ctrl = 4
    if f1(senha)== False:
        ctrl -= 1
        print("A senha deve ter no mínimo 8 caractéres.")
    if f2(senha)== False:
        ctrl -= 1
        print("A senha deve ter no mínimo uma maiúscula.")
    if f3(senha)== False:
        ctrl -= 1
        print("A senha deve ter no mínimo uma minúscula.")
    if f4(senha)== False:
        ctrl -= 1
        print("A senha deve ter no mínimo um digito numérico.")
    if ctrl == 4:
        return True
    else:
        return False
    
    
