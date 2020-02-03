
# coding: utf-8

# In[1]:


sal = float(input("digite seu salário:"))

if sal > 1250.0:
    sal = (sal * 0.10) + sal
    print("O salário com 10%% de aumento é %.2f" % sal)
if sal <= 1250.0:
    sal = (sal * 0.15) + sal
    print("O salário com 15%% de aumento é %.2f" % sal)

