
# coding: utf-8

# In[1]:


litros = int(input("digite a quantidade de litros: "))
tipo = input("digite A se for álcool ou G se for gasolina: ")

precoA = litros*2.4
precoG = litros*4

if tipo =="A":
    if litros<=20:
        precoA = precoA - (precoA*0.03)
        print("o valor final é %.2f" % precoA)
    else:
        precoA = precoA - (precoA*0.05)
        print("o valor final é %.2f" % precoA)
else:
    if litros<=20:
        precoG = precoG - (precoG*0.04)
        print("o valor final é %.2f" % precoA)
    else:
        precoG = precoG - (precoG*0.06)
        print("o valor final é %.2f" % precoA)

