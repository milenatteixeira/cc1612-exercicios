
# coding: utf-8

# In[1]:


mes = input("digite o mes minusculo: ")
dia = int(input("digite o dia: "))

if (dia == 20) and (mes=="março"):
    print("outono.")
    
elif (dia==21) and (mes=="junho"):
    print("inverno.")

elif (dia==22) and (mes=="setembro"):
    print("primavera.")

elif (dia==21) and (mes=="dezembro"):
    print("verão.")

else:
    print("não soube fazer a lógica, professor. sorry.")

