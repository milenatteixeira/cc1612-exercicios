
# coding: utf-8

# In[1]:


notaLetra = input("digite a nota em letra maiúscula: ")

if notaLetra == "A+" or notaLetra == "A":
    print("%s = 5.0" % notaLetra)
elif notaLetra == "A-":
    print("%s = 4.5" % notaLetra)
elif notaLetra == "B+":
    print("%s = 4.0" % notaLetra)
elif notaLetra == "B":
    print("%s = 3.5" % notaLetra)
elif notaLetra == "B-":
    print("%s = 3.0" % notaLetra)
elif notaLetra == "C+":
    print("%s = 2.5" % notaLetra)
elif notaLetra == "C":
    print("%s = 2.0" % notaLetra)
elif notaLetra == "C-":
    print("%s = 1.5" % notaLetra)
elif notaLetra == "D+":
    print("%s = 1.0" % notaLetra)
elif notaLetra == "D":
    print("%s = 0.5" % notaLetra)
elif notaLetra == "F":
    print("%s = 0.0" % notaLetra)
else:
    print("nota invalida. digite uma nota correta.")

