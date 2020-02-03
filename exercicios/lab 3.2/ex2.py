
# coding: utf-8

# In[1]:


lados = int(input("digite o número de lados: "))

if (lados >= 3) and (lados <=10):
    if lados == 3:
        print("triângulo.")
    elif lados == 4:
        print("quadrilátero.")
    elif lados == 5:
        print("pentágono.")
    elif lados == 6:
        print("hexágono.")
    elif lados == 7:
        print("heptágono.")
    elif lados == 8:
        print("octágono.")
    elif lados == 9:
        print("eneágono.")
    elif lados == 10:
        print("decágono.")
else:
    print("o número de lados incorreto. deve ser de 3 a 10. ")

