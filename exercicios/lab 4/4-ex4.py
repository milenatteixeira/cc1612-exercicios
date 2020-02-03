
# coding: utf-8

# In[1]:


from random import randrange
maior=0
i=0
for x in range(0,21):
    numero = randrange(1,101)
    if numero>maior:
        maior=numero
        i+=1
print("O maior número é %d" %maior)
print("O número de atualizações foi de %d"%i)

