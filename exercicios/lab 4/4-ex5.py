
# coding: utf-8

# In[1]:


somatorio = 0
contador = 0
while contador<5:
    nota = float(input("Digite a nota: "))
    somatorio = somatorio + nota
    contador+=1
print("A média aritmética é %.2f"%(somatorio/contador))

