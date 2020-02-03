
# coding: utf-8

# In[ ]:


coluna= input("digite uma coluna :")
linha =int(input("digite a linha :"))

if (coluna== "a" or coluna =="c" or coluna =="e" or coluna =="g") and linha%2== 0:
    print("branco")
if (coluna== "a" or coluna =="c" or coluna =="e" or coluna =="g") and linha%2!= 0 :
    print("preto")
elif (coluna== "b" or coluna =="d" or coluna =="f" or coluna =="h") and linha%2== 0:
    print("preto")
elif (coluna== "b" or coluna =="d" or coluna =="f" or coluna =="h") and linha%2!= 0:
    print("branco")

