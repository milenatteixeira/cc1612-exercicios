
# coding: utf-8

# In[1]:


a = int(input("digite a:"))
b = int(input("digite b:"))
c = int(input("digite c:"))

if (a**2)==(b**2)+(c**2):
    print("Triangulo Retangulo.")
if (a**2)>(b**2)+(c**2):
    print("Triangulo obtusângulo.")
if (a**2)<(b**2)+(c**2):
    print("Triangulo acutângulo.")

