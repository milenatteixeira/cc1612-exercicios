
# coding: utf-8

# In[1]:


n1 = int(input("digite um número: "))
n2 = int(input("digite um número: "))
n3 = int(input("digite um número: "))
print("\nNão Ordenado")
print("N1 : %d; N2: %d; N3: %d"%(n1,n2,n3))
if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux
if n1 > n3:
    aux = n1
    n1 = n3
    n3 = aux
if n2 > n3:
    aux = n2
    n2 = n3
    n3 = aux
print("\nOrdenado")
print("N1 : %d; N2: %d; N3: %d"%(n1,n2,n3))

