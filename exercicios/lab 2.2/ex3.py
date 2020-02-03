
# coding: utf-8

# In[1]:


from math import *
x = int(input("Digite um número a ser atribuido à 'x':"))

if x>5:
    y = ((sqrt(log((x**3))+(3.14**2)+1))-log((x**5)))/((exp(x))+(x**2)+(3**x))
    print(y)
else:
    y = ((sin(x)**2)+(cos(x)**2)+(abs(x)))
    print(y)

