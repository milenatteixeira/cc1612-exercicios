
# coding: utf-8

# In[1]:


cont=0;
q1 = input("Telefonou para a vítima? ")
if q1=="sim":
    cont+=1
q2 = input("Esteve no local do crime? ")
if q2=="sim":
    cont+=1
q3 = input("Mora perto da vítima? ")
if q3=="sim":
    cont+=1
q4 = input("Devia para a vítima? ")
if q4=="sim":
    cont+=1
q5 = input("Já trabalhou com a vítima? ")
if q5=="sim":
    cont+=1


if cont==2:
    print("suspeito")
elif cont>=3 and cont<=4:
    print("cúmplice")
elif cont==5:
    print("culpado.")
else:
    print("inocente.")

