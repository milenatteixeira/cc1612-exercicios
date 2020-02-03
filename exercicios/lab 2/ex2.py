
# coding: utf-8

# In[1]:


km = int(input("digite a quantidade de km percorridos: "))
dias = int(input("digite a quantidade de dias em que o veículo ficou alugado: "))

preco = (0.15*km) + (60*dias)

print("o valor a ser pago é %.2f" % preco)

