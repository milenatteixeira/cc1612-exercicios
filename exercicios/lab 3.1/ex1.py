
# coding: utf-8

# In[1]:


nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))

media = (nota1+nota2)/2

if media==10:
    print("aprovado com distinção.")
else:
    if media>=5:
        print("aprovado.")
    else:
        print("reprovado.")

