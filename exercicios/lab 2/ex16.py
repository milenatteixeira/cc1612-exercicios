
# coding: utf-8

# In[1]:


n1 = float(input("nota 1:"))
n2 = float(input("nota 2:"))
n3 = float(input("nota 3:"))

m = (n1+(n2*2)+(n3*3))/6

if m >=5:
    print("Media = %.2f. Aprovado." %m)
else:
    print("Media = %.2f. Reprovado" %m)

