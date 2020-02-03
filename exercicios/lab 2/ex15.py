
# coding: utf-8

# In[1]:


km = int(input("digite a kilometragem:"))

if km <= 200:
    preco = km * 0.5
    print("O preço da passagem é R$%.2f" % preco)
else:
    preco = km * 0.45
    print("O preço da passagem é R$%.2f" %preco)

