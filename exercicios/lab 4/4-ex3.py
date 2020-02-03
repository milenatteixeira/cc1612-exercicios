
# coding: utf-8

# In[1]:


print("Digite um número que seja de 0 a 10.")
num = int(input("Número: "))

while num<=0 or num>=10:
    print("Número inválido. Digite novamente.")
    num = int(input("Número: "))
print("Número aceito.")

