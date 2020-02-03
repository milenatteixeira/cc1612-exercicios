
# coding: utf-8

# In[1]:


ingresso = 0
while True:
    idade = input("Digite a idade: ")
    if idade!="":
        idade=int(idade)
        if idade<=2:
            ingresso = ingresso
        elif idade>=3 and idade<=12:
            ingresso = ingresso + 14
        elif idade>=65:
            ingresso = ingresso + 18
        else:
            ingresso = ingresso + 23
    else:
        print(ingresso)
        break

