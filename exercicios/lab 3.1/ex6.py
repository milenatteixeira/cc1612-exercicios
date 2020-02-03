
# coding: utf-8

# In[1]:


from math import*
a = int(input("digite a: "))
if a == 0:
    print("a equação não é do segundo grau.")
else:
    b = int(input("digite b: "))
    c = int(input("digite c: "))

    delta = (b**2)-(4*a*c)

    if delta<=0:
        print("a equação não possui raízes reais.")
    elif delta==0:
        print("a equação possui apenas uma raíz.")
        x1 = ((-b)+(sqrt(delta)))/(2*a)
        print("x = %d" % x1)
    else:
        print("a equação possui duas raízes reais.")
        x1 = ((-b)+(sqrt(delta)))/(2*a)
        x2 = ((-b)-(sqrt(delta)))/(2*a)
        print("x1 = %d" % x1)
        print("x2 = %d" % x2)

