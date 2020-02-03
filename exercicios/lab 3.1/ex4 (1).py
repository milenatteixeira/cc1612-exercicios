
# coding: utf-8

# In[1]:


salario = float(input("digite o salário: "))

if salario>=0 and salario<=400:
    aumento = salario*0.15
    salario = salario + aumento
    print("aumento: %.2f" % aumento)
    print("salário com 15%% é %.2f" % salario)
elif salario>=400.01 and salario<=800.00:
    aumento = salario*0.12
    salario = salario + aumento    
    print("aumento: %.2f" % aumento)
    print("salário com 12%% é %.2f" % salario)
elif salario>=800.01 and salario<=1200.00:
    aumento = salario*0.10
    salario = salario + aumento
    print("aumento: %.2f" % aumento)
    print("salário com 10%% é %.2f" % salario)
elif salario>=1200.01 and salario<=2000.00:
    aumento = salario*0.07
    salario = salario + aumento
    print("aumento: %.2f" % aumento)
    print("salário com 7%% é %.2f" % salario)
else:
    aumento = salario*0.04
    salario = salario + aumento
    print("aumento: %.2f" % aumento)
    print("salário com 4%% é %.2f" % salario)

